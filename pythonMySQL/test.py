import mysql.connector
import config


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=config.USER_PASS,
)

print(db)
    
