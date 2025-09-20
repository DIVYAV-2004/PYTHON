#Python DataBase Connection/Connectivity (PDBC)
#method1
import mysql.connector

from db import info
try:
    mysql.connector.connect(**info)
    print('connection successful')
except:
    print('not able to connect')

#method2
import mysql.connector
info={
    'user':'root',
    'password':'Divyav@2004',
    'host':'localhost',
    'port':3306
}
try:
    mysql.connector.connect(**info)
    print('connection successful')
except:
    print('not able to connect')

#method3
import mysql.connector

try:
    mysql.connector.connect(
    user='root',
    password='Divyav@2004',
    host='localhost',
    port=3306
)
    print('connection successful')
except:
    print('not able to connect')


