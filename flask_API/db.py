import sqlite3

# Connect Object establishes a conenction with the Data Base/ File
conn = sqlite3.connect("books.sqlite")

# Cursor helps you to execute SQL Statements in the Data Base/ File
cursor = conn.cursor() 

sql_query = """ CREATE TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""

cursor.execute(sql_query)