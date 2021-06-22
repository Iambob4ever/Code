#!/usr/bin/env python3
import configparser
import mysql.connector
from mysql.connector import Error

#This class is specifically for getting the config to connect to a mysql db
class sql_config():
  
      def __init__(self,config_location):
        config = configparser.ConfigParser()
        config.read(config_location)
        self.host = config['laptop_db']['host']
        self.db_name = config['laptop_db']['db_name']
        self.user = config['laptop_db']['user']
        self.passwd = config['laptop_db']['pass']


def create_connection(db_config):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=db_config.host,
            db = db_config.db_name,
            user=db_config.user,
            passwd=db_config.passwd
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

#calls the connection function
laptop_sql = sql_config('test.config')
print(laptop_sql.host)
laptopdb_connection = create_connection(laptop_sql)




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