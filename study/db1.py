import mysql.connector

dbconnection = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = '161537'
)

print(dbconnection)

x = dbconnection.cursor()
#x.execute('create database test1')
x.execute('show databases')

for i in x:
    print(i)

print('My name is '{1}{2}'.format('Htet','Aung'))

