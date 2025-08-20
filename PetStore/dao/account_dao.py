#coding = utf-8

from dao.base_dao import BaseDao

class AccountDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findbyid(self, userid):
            """ 按照用户ID查找用户信息 """

            account = None
            try:
                # 创建游标对象
                with self.conn.cursor() as cursor:
                    # 3. 执行SQL操作
                    sql = "select userid,password,email,name,addr,city,country,phone from accounts where userid =%s"
                    cursor.execute(sql, userid)

                    # 4.提取结果集
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
