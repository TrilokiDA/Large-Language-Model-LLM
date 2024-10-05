# Created by trilo at 04-10-2024
import sqlite3

# connect to sqlite3
conn = sqlite3.connect("student.db")

# create a cursor object
cursor = conn.cursor()

# create table
table_info = """
CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

# insert records
cursor.execute("""INSERT INTO STUDENT values('ABC', 'BE', 'A', 85)""")
cursor.execute("""INSERT INTO STUDENT values('DEF', 'BA', 'B', 90)""")
cursor.execute("""INSERT INTO STUDENT values('GHI', 'MA', 'A', 50)""")
cursor.execute("""INSERT INTO STUDENT values('JKL', 'B.Tech', 'B', 80)""")
cursor.execute("""INSERT INTO STUDENT values('MNO', 'B.Sc', 'B', 75)""")
cursor.execute("""INSERT INTO STUDENT values('PQR', 'M.SC', 'A', 60)""")

# display the records
print("Inserted records are:")

data = cursor.execute("""SELECT * FROM STUDENT""")
for row in data:
    print(row)

# close connection
conn.commit()
conn.close()
