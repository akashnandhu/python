
import mysql.connector
connection=mysql.connector.connect("""
host="local host"
user="root"
password=""
database="nandhu"
""")
cursor=connection.cursor
cursor.execute("""
     CREATE TABLE IF NOT EXISTS students (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name VARCHAR(20) NOT NULL,
         age INTEGER,
         gender VARCHAR(20),
         email VARCHAR(30) UNIQUE,
         phone VARCHAR(30)
     )
  """)