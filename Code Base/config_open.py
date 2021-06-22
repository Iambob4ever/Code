#!/usr/bin/env python3
import configparser
import mysql.connector
from mysql.connector import Error




######################################################################
#This section gets the values from the config. This should be a class 
config = configparser.ConfigParser()
config.read('test.config')
host = config['laptop_db']['host']
db_name = config['laptop_db']['db_name']
user = config['laptop_db']['user']
passwd = config['laptop_db']['pass']


def create_connection(host_name, db_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            db = db_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

#calls the connection function
laptopdb_connection = create_connection(host,db_name,user,passwd)

#This line is the sql command. Bacially python just jams it in as a string
sql_q = "INSERT INTO remote_test (value, user) VALUES (%s, %s)"

#Data to input goes here
val = (4,"python")

#Creates a curser, the .execute function feeds the sql command, and the 2nd variable is variables to input
db_curser = laptopdb_connection.cursor()
db_curser.execute(sql_q, val)
laptopdb_connection.commit()


#Pulls the entiry where value =3
sql_q2 = "SELECT * FROM remote_test WHERE value=3"
db_curser.execute(sql_q2)
results = db_curser.fetchall()

#Note, the sql db has a timestamp field which adds to the entry when it was committed.
print(results)