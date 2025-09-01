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
        insert into student(s_id, s_name , s_sex , s_birthday)
        values (%s, %s, %s, %s)
        '''
        cursor.execute(sql,[201 , 'marry', 0 , '2010-04-04'])
        connection.commit()
        print("input scussful")
    
except pymysql.DatabaseError as e:
    print(e)
    connection.rollback()

finally :
    connection.close() 