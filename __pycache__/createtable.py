import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",        
    database="school"   
)

print("Connection successful!")


mydb.close()