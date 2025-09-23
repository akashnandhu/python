import sqlite3
connection = sqlite3.connect("akashs.db")
cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(20) NOT NULL,
        age INT,
        gender VARCHAR(20),
        email VARCHAR(30) UNIQUE,
        phone VARCHAR(30)
    )
 """)
cursor.execute("""
INSERT INTO student(name,age,gender,email,phone)VALUES
               ("akhila",45,"male","akhila004@gamil.com","46584479213")
""")

cursor.execute("SELECT * FROM student")
rows=cursor.fetchall()
for row in rows:
    print(row)


try:
    cursor.execute("""
        UPDATE student
        SET email='jebin6884@gmail.com'
        WHERE name='akhila'
    """)
except sqlite3.IntegrityError as e:
    print("Update failed due to constraint:", e)


# cursor.execute("""
# DELETE FROM student WHERE name="nandhu" 
# """)


connection.commit()
connection.close()


