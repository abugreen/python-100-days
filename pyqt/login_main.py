import sys
from PyQt6.QtWidgets import *

from login_6 import Ui_Form


class MyWidget(Ui_Form , QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
           
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWidget()
    app.exec() 