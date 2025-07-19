from mysql.connector import connect
try:
    host='localhost'
    user='root'
    passwd=''
    database='my_first_python_db'
    db_connection=connect(host=host,user=user,passwd=passwd,database=database)
    print(db_connection)
    
except Exception as e:
    print(e)