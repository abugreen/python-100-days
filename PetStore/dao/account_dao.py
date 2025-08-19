#coding = utf-8

from base_dao import BaseDao

class AccountBao(BaseDao):
    def __init__(self):
        super().__init__()
        
        
    def findbyid(self, userid):
        account = None
        
        try:
            with self.conn.cursor() as cursor:
                sql = "select userid, password, name , addr , city , country , phone , from , accounts where userid = %s"
                cursor.execute(sql, userid)
                
                row = cursor.fetchone()
                if row is not None:
                    # 创建空字典
                    account = {}

                    account['userid'] = row[0]
                    account['password'] = row[1]
                    account['email'] = row[2]
                    account['name'] = row[3]
                    account['addr'] = row[4]
                    account['city'] = row[5]
                    account['country'] = row[5]
                    account['country'] = row[6]
                    account['phone'] = row[7]
        finally:
                # 关闭连接
            self.close()
        return account          
