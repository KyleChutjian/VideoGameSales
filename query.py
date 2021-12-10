from google.cloud.sql.connector import connector
import json
import os
import csv
import plotly.express as px
import pandas as pd

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

def query():
    # Setup
    cur.execute('USE vgsales')

    # Sales by Rank
    df = pd.read_sql('''
        SELECT name as 'Game Name', na_sales, eu_sales, jp_sales, other_sales
        FROM Game
        ORDER BY global_sales DESC;
    ''', cnx)
    fig = px.bar(df, title='Sales By Game', x='Game Name', y=['na_sales', 'eu_sales', 'jp_sales', 'other_sales'])
    fig.show()

    # Pie Chart of Publishers
    pie_df = pd.read_sql('''
        SELECT publisher_name as 'Publisher', COUNT(publisher_name) as 'Number of Games'
        FROM Publisher
        GROUP BY publisher_name
        ORDER BY COUNT(publisher_name) DESC;
    ''', cnx)
    pie_fig = px.pie(pie_df, title='Percent of Games by Platform', values='Number of Games', names='Publisher')
    pie_fig.update_traces(textposition='inside', textinfo='percent+label')
    pie_fig.show()

    # Sales by Publisher Bar Chart
    publisher_barchart_df = pd.read_sql('''
        SELECT p.publisher_name as 'Publisher', SUM(g.na_sales) as 'NA Sales', SUM(g.eu_sales) as 'EU Sales', SUM(g.jp_sales) as 'JP Sales', SUM(g.other_sales) as 'Other Sales'
        FROM Game g, Publisher p
        WHERE g.publisher_id = p.publisher_id
        GROUP BY g.publisher_id
        ORDER BY SUM(g.global_sales) DESC;
    ''', cnx)
    publisher_barchart_fig = px.bar(publisher_barchart_df, title='Sales by Publisher', x='Publisher', y=['NA Sales', 'EU Sales', 'JP Sales', 'Other Sales'])
    publisher_barchart_fig.show()

    # Sales by Genre Bar Chart
    genre_barchart_df = pd.read_sql('''
        SELECT genre.genre_name as 'Genre', SUM(g.na_sales) as 'NA Sales', SUM(g.eu_sales) as 'EU Sales', SUM(g.jp_sales) as 'JP Sales', SUM(g.other_sales) as 'Other Sales'
        FROM Game g, Genre genre
        WHERE g.genre_id = genre.genre_id
        GROUP BY g.genre_id
        ORDER BY SUM(g.global_sales) DESC;
    ''', cnx)
    genre_barchart_fig = px.bar(genre_barchart_df, title='Sales by Genre', x='Genre', y=['NA Sales', 'EU Sales', 'JP Sales', 'Other Sales'])
    genre_barchart_fig.show()

    # Number of Games
    year_linechart_df = pd.read_sql('''
        SELECT year as 'Year', COUNT(*) as 'Number of Games'
        FROM Game
        GROUP BY year
        ORDER BY year;
    ''', cnx)
    year_linechart_fig = px.line(year_linechart_df, title='Number of Games By Year', x='Year', y='Number of Games')
    year_linechart_fig.show()


print("Connecting")
cnx = make_connection()
cur = cnx.cursor()
print("Querying")
query()
cur.close()
cnx.commit()
cnx.close()
print("Done")
