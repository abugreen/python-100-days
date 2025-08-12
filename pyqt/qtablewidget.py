from PyQt5.QtWidgets import *
import sys

data = [['0036','高等數學','李敖','人名郵電出版社','20000812','1'],
        ['0004','flah','留洋','中國出版社','19990312','2']]

column_names = ['書籍編號','書籍名稱','作者','出版社','出版日期','庫存數量']


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("qcombobox")
        layout = QFormLayout(self)

        box = QComboBox()
        box.addItem("c++")
        box.addItem("c")
        box.addItems(["java", "python"])
        box.currentIndexChanged.connect(self.selectionchange)

        layout.addRow(QLabel("choice your language"),box)

  
    def selectionchange(self, item):
        print(item.text())