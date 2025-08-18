# coding=utf-8
# 代码文件：code/chapter11/PetStore/dao/product_dao.py

"""商品管理DAO"""

from base_dao import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findall(self):
        """ 查询所有商品数据 """

        # 定义商品列表
        products = []
        try:
            # 创建游标对象
            with self.conn.cursor() as cursor:
                # 3. 执行SQL操作
                sql = 'select productid,category,cname,ename,image,listprice,unitcost,descn ' \
                      ' from products'
                cursor.execute(sql)

                # 4.提取结果集
                result_set = cursor.fetchall()

                for row in result_set:
                    # 创建空字典保存一条数据
                    product = {}

                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listprice'] = float(row[5])
                    product['unitcost'] = float(row[6])
                    product['descn'] = row[7]

                    # 把商品添加到商品列表
                    products.append(product)

        finally:
            # 关闭连接
            self.close()

        return products

    def findbycat(self, catname):
        """ 根据商品类别查询商品数据 """

        # 定义商品列表
        products = []
        try:
            # 创建游标对象
            with self.conn.cursor() as cursor:
                # 3. 执行SQL操作
                sql = 'select productid,category,cname,ename,image,listprice,unitcost,descn ' \
                      ' from products where category=%s'
                cursor.execute(sql, catname)

                # 4.提取结果集
                result_set = cursor.fetchall()

                for row in result_set:
                    # 创建空字典保存一条数据
                    product = {}

                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listprice'] = float(row[5])
                    product['unitcost'] = float(row[6])
                    product['descn'] = row[7]

                    # 把商品添加到商品列表
                    products.append(product)

        finally:
            # 关闭连接
            self.close()

        return products

    def findbyid(self, productid):
        """ 根据商品id查询商品数据 """

        # 返回商品
        product = None
        try:
            # 创建游标对象
            with self.conn.cursor() as cursor:
                # 3. 执行SQL操作
                sql = 'select productid,category,cname,ename,image,listprice,unitcost,descn ' \
                      ' from products where productid=%s'
                cursor.execute(sql, productid)

                # 4.提取结果集
                row = cursor.fetchone()

                if row is not None:
                    # 创建空字典保存一条数据
                    product = {}

                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listprice'] = float(row[5])
                    product['unitcost'] = float(row[6])
                    product['descn'] = row[7]

        finally:
            # 关闭连接
            self.close()

        return product