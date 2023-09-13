import mysql.connector
from mysql.connector  import Error
import pandas as pd


def create_server_connection(host_name,user_name,user_password):
  connection = None
  try:
    connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        passwd = user_password
    )
    print("connection successful")
    return connection
  except Error as err:
    print(f"1Error:'{err}'")
    

    # Put Mysql terminal password
userdb = "root"
pw = "12345"
#Database name
db = 'mysql_python'
connection = create_server_connection("127.0.0.1",userdb,pw)


#create mysql_python
def create_database(connection,query):
  cursor = connection.cursor()
  try:
    cursor.execute(query)
    print("Database create successfully")
  except Error as err:
        print(f"3Error:'{err}'")
      
create_server_query = "Create database mysql_python"
create_database(connection,create_server_query)

#connect to database
def create_db_connection(host_name,user_name,user_password,db_name):
  
  try:
    connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        passwd = user_password,
        database = db_name)
    print("My SQL database connection successfull")
    return connection
  except Error as err:
        print(f"2Error:'{err}'")

connection = create_db_connection("127.0.0.1",userdb,pw,db)
        

#Execute sql queries
def execute_query(connection,query):
  cursor = connection.cursor()
  try:
    cursor.execute(query)
    connection.commit()
    print("Query was succesfull")
  except Error as err:
        print(f"4Error:'{err}'")

#create table for Channel details

create_channels_table = """
CREATE TABLE channels (
  channel_id VARCHAR(255),
  channel_name VARCHAR(255) NOT NULL,
  playlist_id VARCHAR(50) NOT NULL,
  subscribers INT,
  views INT,
  total_videos INT,
  description VARCHAR(5000) NOT NULL,
  country VARCHAR(50)
)
"""
execute_query(connection,create_channels_table)

#connect to db


#create table for video details
create_videos_table = """
CREATE TABLE videos (
  channel_name VARCHAR(50) NOT NULL,
  channel_id VARCHAR(255) NOT NULL,
  video_id VARCHAR(50) NOT NULL,
  title VARCHAR(100) NOT NULL,
  tags JSON,
  thumbnail VARCHAR(255),
  description TEXT,
  published_date DATETIME NOT NULL,
  duration VARCHAR(50),
  views INT,
  likes INT ,
  comments INT,
  favorite_count INT,
  definition VARCHAR(100),
  caption_status VARCHAR(255)
)
"""
execute_query(connection,create_videos_table)

create_comments_table = """
CREATE TABLE comments (
  comment_id VARCHAR(255),
  video_id VARCHAR(50) NOT NULL,
  comment_text TEXT,
  comment_author VARCHAR(255),
  comment_posted_date VARCHAR(50),
  like_count INT,
  reply_count INT
)
"""
execute_query(connection,create_comments_table)
user_input = input("Enter delete or no: ")
if user_input == 'delete':
   cursor = connection.cursor()
   cursor.execute('DROP DATABASE mysql_python')
