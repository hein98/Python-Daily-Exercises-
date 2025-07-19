from mysql.connector import connect
try:
    host=input('host: ')
    user=input('user: ')
    passwd=input('passwd: ')
    mysql_connection=connect(host=host,user=user,passwd=passwd)
    cursor=mysql_connection.cursor()
    cursor.execute('CREATE DATABASE my_first_python_db;')
    print('Database created successfully')
    
except Exception as e:
    print(e)