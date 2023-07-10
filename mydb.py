import mysql.connector

dataBase= mysql.connector.connect(host='localhost',user='root',passwd='pass123')

cursorObj=dataBase.cursor()

cursorObj.execute("CREATE DATABASE forfun")
