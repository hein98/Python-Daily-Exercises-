from mysql.connector import connect

try:
    host=input('Host: ')
    port=3307
    user=input('User: ')
    passwd=input('password: ')
    
    db_connection=connect(host=host,port=port,user=user,passwd=passwd)
    print(db_connection)
except Exception as e:
    print(e)