# from account_dao import *
from product_dao import *

# dao = AccountDao()
# data = dao.findbyid('j2ee')

dao = ProductDao()
# data = dao.findall()
# data = dao.findbycat('鸟类')
# print(data)

data = dao.findbyid('AV-CB-01')
print(data)
