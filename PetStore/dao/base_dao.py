#coding = utf-8

import pymysql
from db_config import *

class BaseDao(object):
    def __init__(self):
        host = DB_HOST
        user = DB_USER
        port = DB_PORT
        password = DB_PASSWORD
        database = DB_DATABASE
        charset = DB_CHARSET
        
        self.conn = pymysql.connect(host=host, 
                                    user=user, 
                                    port=port, 
                                    password=password, 
                                    database=database, 
                                    charset=charset
                                    )
        
    def close(self):
        self.conn.close()
        