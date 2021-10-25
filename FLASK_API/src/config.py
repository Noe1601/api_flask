# from re import DEBUG

# from flask import config


# class DevelopmentConfig():
#     DEBUG = True
#     MYSQL_HOST = 'localhost'
#     MYSQL_USER = 'root'
#     MYSQL_PASSWORD = '123456'
#     MYSQL_DB = 'COLEGIO'
#     MYSQL_PORT=3306


# config = {
#     'development': DevelopmentConfig
# }

import mysql.connector


database = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="123456",
    database="COLEGIO",
    port=3306
)
