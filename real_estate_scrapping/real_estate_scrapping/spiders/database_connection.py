import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nauka2012Podaci",
    database="real_estate"
)

db_cursor = db_connection.cursor()

