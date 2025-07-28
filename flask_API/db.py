import pymysql

# Connect Object establishes a conenction with the Data Base/ File
conn = pymysql.connect(
    host='sql12.freesqldatabase.com',
    database='sql12792377',
    user='sql12792377',
    password='wqkZMQLy3J',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Cursor helps you to execute SQL Statements in the Data Base/ File
cursor = conn.cursor() 

sql_query = """ CREATE TABLE book (
    id integer PRIMARY KEY AUTO_INCREMENT,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL )
"""

cursor.execute(sql_query)
conn.close()