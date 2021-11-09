from google.cloud.sql.connector import connector
import json
import os
import csv

# Written by Kyle Chutjian and Thomas Eckert


# Reading Credentials JSON File
f = open('Data/credentials.json')
credentials = json.load(f)
f.close()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials["GOOGLE_APPLICATION_CREDENTIALS"]

# make the connection to the db
def make_connection():
    return connector.connect(
        credentials["instanceName"],
        "pymysql",
        user=credentials["username"],
        password=credentials["password"],
        database=None
    )

def setup_db(cur):
    # Set up db
    cur.execute('CREATE DATABASE IF NOT EXISTS vgsales')
    cur.execute('USE vgsales')

    cur.execute('DROP TABLE IF EXISTS Game;')
    cur.execute('DROP TABLE IF EXISTS Genre;')
    cur.execute('DROP TABLE IF EXISTS Publisher;')
    cur.execute('DROP TABLE IF EXISTS Platform;')

    cur.execute('''
        CREATE TABLE Genre (
            genre_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            genre_name VARCHAR(50) NOT NULL)
    ''')

    cur.execute('''
        CREATE TABLE Publisher (
            publisher_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            publisher_name VARCHAR(50) NOT NULL)
    ''')

    cur.execute('''
        CREATE TABLE Platform (
            platform_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            platform_name VARCHAR(50) NOT NULL)
    ''')

    cur.execute('''
        CREATE TABLE Game (
            rank INT NOT NULL,
            name VARCHAR(50) NOT NULL,
            platform_id INT NOT NULL,
            year INT NOT NULL,
            genre_id INT NOT NULL,
            publisher_id INT NOT NULL,
            na_sales INT NOT NULL,
            eu_sales INT NOT NULL,
            jp_sales INT NOT NULL,
            other_sales INT NOT NULL,
            global_sales INT NOT NULL,
            FOREIGN KEY(genre_id) REFERENCES Genre(genre_id),
            FOREIGN KEY(publisher_id) REFERENCES Publisher(publisher_id),
            FOREIGN KEY(platform_id) REFERENCES Platform(platform_id),
            PRIMARY KEY(rank)
            )
    ''')

def insert_data(cur):
    cur.execute('USE vgsales')


    # Reading from CSV File
    rows = []
    file = open('sample.csv', encoding='utf-8-sig')
    csvreader = csv.reader(file)
    header = next(csvreader)

    for row in csvreader:
        rows.append(row)
        cur.execute('''INSERT IGNORE INTO Platform (platform_name)
            VALUES ( %s )''', (row[2]))

        cur.execute('''INSERT IGNORE INTO Genre (genre_name)
            VALUES ( %s )''', (row[4]))

        cur.execute('''INSERT IGNORE INTO Publisher (publisher_name)
            VALUES ( %s )''', (row[5]))

        cur.execute('SELECT platform_id FROM Platform WHERE platform_name = %s ', (row[2],))
        platform_id = cur.fetchone()[0]

        cur.execute('SELECT genre_id FROM Genre WHERE genre_name = %s ', (row[4],))
        genre_id = cur.fetchone()[0]

        cur.execute('SELECT publisher_id FROM Publisher WHERE publisher_name = %s ', (row[5],))
        publisher_id = cur.fetchone()[0]


        cur.execute('''INSERT IGNORE INTO Game
            (Rank, Name, platform_id, Year, genre_id, publisher_id, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales)
            
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                    (row[0], row[1], platform_id, row[3], genre_id, publisher_id, row[6], row[7], row[8], row[9], row[10]))
    file.close()

    print(header)
    print(rows[0])

cnx = make_connection()
cur = cnx.cursor()
print("Starting Setup...")
setup_db(cur)
print("Finished Setup.")
print("Starting Insert...")
insert_data(cur)
print("Finished Insert.")
cur.close()
cnx.commit()
cnx.close()
print("FINISHED")