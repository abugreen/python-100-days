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
        self.setWindowTitle("qtablewidget")
        self.resize(800,600)
       
        layout = QVBoxLayout(self)
        table = QTableWidget()
        layout.addWidget(table)
        table.setRowCount(len(data))
        table.setColumnCount(len(column_names))
        table.setHorizontalHeaderLabels(column_names)
        horizontalHeader = table.horizontalHeader()
        # horizontalHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        for row in range(len(data)):
            for col in range(len(column_names)):
                table.setItem(row, col, QTableWidgetItem(data[row][col]))

        table.itemSelectionChanged.connect(self.click_success)

    def click_success(self):
        table = self.sender()
        row = table.currentRow()
        col = table.currentColumn()
        print(data[row][col])



def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()