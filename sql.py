import pymysql
from dotenv import load_dotenv
import os
load_dotenv()

MY_SQL_DB_PASSWORD = os.getenv('MY_SQL_DB_PASSWORD')
my_db = pymysql.connect(
    host='localhost',
    user='root', 
    port=3306,
    password=MY_SQL_DB_PASSWORD,
    database='Students')

my_cursor = my_db.cursor()

# table_info = '''
# Create table Students.Student(NAME VARCHAR(25) NOT NULL, AGE INT NOT NULL, DEPARTMENT VARCHAR(25) NOT NULL);
# '''
# my_cursor.execute(table_info)

my_cursor.execute('''Insert into Students.Student values('Catherine',25,'Data Science')''')
my_cursor.execute('''Insert into Students.Student values('Peter',38,'Web Development')''')
my_cursor.execute('''Insert into Students.Student values('Luke',30,'Management')''')
my_cursor.execute('''Insert into Students.Student values('John',27,'Software Development')''')
my_cursor.execute('''Insert into Students.Student values('Romeo',22,'Networking')''')
my_db.commit()

print("Inserted Rows are...")
my_cursor.execute('''Select * from Students.Student''')
for row in my_cursor.fetchall():
    print(row)

my_db.close()
