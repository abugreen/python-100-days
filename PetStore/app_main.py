#coding = utf8

import os
import sys
from PyQt5.QtWidgets import *
import ui.login
from dao.account_dao import AccountBao

def btnok_click():
    print("click")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    loginform = ui.login.Ui_Form()
    loginform.setupUi(window)
    
    loginform.btn_ok.clicked.connect(btnok_click)
    
    window.show()
    sys.exit(app.exec_())
    