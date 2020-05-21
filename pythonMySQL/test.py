import mysql.connector as mysql
import config
from data import users_info

# mysql database connection with mysql.connector
db = mysql.connect(
    host="localhost",
    user="root",
    passwd=config.USER_PASS,
    database="testdb", # select your database
)

# create object of 'cursor' class which help write sql statments with python
cursor = db.cursor()

# create database
#cursor.execute("CREATE DATABASE testdb")
  
# show list of databases
'''cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
for database in databases:
    print(database)'''

# make table to 'testdb'
'''cursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")'''

# show tables
'''cursor.execute("SHOW TABLES")'''

# create primary key and delete in table users
#cursor.execute("DROP TABLE users")
#cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))") 
#cursor.execute("DESC users")
#print(cursor.fetchall())
#cursor.execute("ALTER TABLE users DROP id")

#cursor.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

# INSERTING DATA IN USERS TABLE
'''query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
values = ("Jonas", "Laurinaitis")
cursor.execute(query, values)
db.commit()
print(cursor.rowcount, "record")'''

# ADDING DATASET FROM DATA.PY TO USERS TABLE
'''cursor.execute("ALTER TABLE users CHANGE user_name cash VARCHAR(255)")
cursor.execute("DELETE FROM users WHERE name='Jonas'")
query = "INSERT INTO users (name, cash) VALUES (%s, %s)"
cursor.executemany(query, users_info)
db.commit()
print(cursor.rowcount, "record inserted")'''

# GET RECORDS FROM USERS TABLE
'''cursor.execute("SELECT * FROM users")
records = cursor.fetchall()
for record in records:
    print(record)'''

'''cursor.execute("SELECT id, name FROM users")
records = cursor.fetchall()
for record in records:
    print(record)'''

'''cursor.execute("SELECT id, name FROM users WHERE id=75")
records = cursor.fetchall()
for record in records:
    print(record)'''

# ORDER BY
'''cursor.execute("SELECT * FROM users ORDER BY cash")
records = cursor.fetchall()
for record in records:
    print(record)'''

# UPDATE DATA
cursor.execute("UPDATE users SET name='JONAS LAURINAITIS' WHERE id = 99")
db.commit()
cursor.execute("SELECT * FROM users")
records = cursor.fetchall()
for record in records:
    print(record)
