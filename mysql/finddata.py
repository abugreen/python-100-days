#coding = utf-8

import pymysql

connection = pymysql.connect(
    host= '127.0.0.1',
    user= 'root',
    port = 3306,
    database='school_db',
    password= '12345678',
    charset= 'utf8')
    

try :
    with connection.cursor() as cursor:
        sql = '''
        select s_id ,s_name , s_sex, s_birthday from student 
        where s_sex = %s
        '''
        cursor.execute(sql,[1])
        rs = cursor.fetchall()
        
        for row in rs:
            message = '{}-學號{}-生日{}'.format(row[1], row[0], row[3])
            print(message)
    
except pymysql.DatabaseError as e:
    print(e)
    connection.rollback()

finally :
    connection.close() 