print("helloworld")


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jockey"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE mydatabase.environment_ref (env_name VARCHAR(255), app_id int(8), repo_url VARCHAR(35), status int(1))")
"""
mycursor.execute("CREATE DATABASE mydatabase")


mycursor.execute("CREATE TABLE Environment_Ref (Env_name VARCHAR(35), App_Id int(8), repo_url VARCHAR(35), status int(1))")
"""