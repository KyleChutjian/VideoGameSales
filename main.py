from google.cloud.sql.connector import connector
import json
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "csc-ser325-325500-571022c3297c.json"


# make the connection to the db
# I am a genus
def make_connection():
    return connector.connect(
        "csc-ser325-325500:us-central1:db-325instance",
        "pymysql",
        user="root",
        password="highfiveme",
        database=None
    )


def setup_db(cur):
    # Set up db
    cur.execute('CREATE DATABASE IF NOT EXISTS roster_db')
    cur.execute('USE roster_db')

    cur.execute('DROP TABLE IF EXISTS Course;')
    cur.execute('DROP TABLE IF EXISTS User;')
    cur.execute('DROP TABLE IF EXISTS Member;')

    cur.execute('''
        CREATE TABLE User (
        id     INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            name   VARCHAR(20) UNIQUE);
        ''');

    cur.execute('''CREATE TABLE Course (
            id     INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            title  VARCHAR(20) UNIQUE);
        ''');

    cur.execute('''CREATE TABLE Member (
            user_id     INT,
            course_id   INT,
            role        INT,
            FOREIGN KEY(user_id) REFERENCES User(id),
            FOREIGN KEY(course_id) REFERENCES Course(id),
            PRIMARY KEY (user_id, course_id)
        );
        ''')


def insert_data(cur):







#     cur.execute('USE roster_db')
#
#     fname = 'roster_data.json'
#
#     # Data structure as follows:
#     #   [
#     #   [ "Charley", "si110", 1 ],
#     #   [ "Mea", "si110", 0 ],
#
#     # open the file and read
#     str_data = open(fname).read()
#     # load the data in a json object
#     json_data = json.loads(str_data)
#
#     # json data is loaded in a pyton list
#     for entry in json_data:
#         name = entry[0]
#         title = entry[1]
#
#         print(name)
#         print(title)
#
#         # INSERT OR IGNORE satisfies the uniqueness constraint. the inserted data will be ignored if we try to add duplicates.
#         # works as both insert and update
#         cur.execute('''INSERT IGNORE INTO User (name)
#             VALUES ( %s )''', (name))
#
#         # look up the primary key from inserted data.
#         cur.execute('SELECT id FROM User WHERE name = %s ', (name,))
#         user_id = cur.fetchone()[0]
#
#         # same technique is used to insert the title
#         cur.execute('''INSERT IGNORE INTO Course (title)
#             VALUES ( %s )''', (title,))
#         cur.execute('SELECT id FROM Course WHERE title = %s ', (title,))
#         course_id = cur.fetchone()[0]
#
#         # insert both keys in the many to many connector table.
#         cur.execute('''INSERT IGNORE INTO Member
#             (user_id, course_id) VALUES ( %s, %s )''',
#                     (user_id, course_id))
#
#
# cnx = make_connection()
# cur = cnx.cursor()
# print("Starting Setup...")
# setup_db(cur)
# print("Finished Setup.")
# print("Starting Insert...")
# insert_data(cur)
# print("Finished Insert.")
# cur.close()
# cnx.commit()
# cnx.close()
# print("FINISHED")
