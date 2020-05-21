import mysql.connector as mysql
import config

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


    
