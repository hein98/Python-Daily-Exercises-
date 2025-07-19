from mysql.connector import connect

try:
    db_connection=connect(host='localhost',user='root',passwd='',database='my_first_python_db')
    
    sql='''
        CREATE TABLE employees(
            employee_id INT(20),
            first_name VARCHAR(50)
        )
        '''
    cursor=db_connection.cursor()
    cursor.execute(sql)
    print('Tables added successfully')
    
except Exception as  e:
    print(e)
    