import mysql.connector

dbconnection = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = '161537'
)

print(dbconnection)

x = dbconnection.cursor()
#x.execute('create database test2')

x.execute('show databases')

for i in x:
    print(i)




