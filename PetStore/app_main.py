#coding = utf8

import os
import sys
from PyQt5.QtWidgets import *
import ui.login
from dao.account_dao import AccountBao

def btnok_click():
    username = loginform.user_name.text()
    password = loginform.password.text()
    dao = AccountBao()
    account = dao.findbyid(username)
    if account is not None and account['password'] == password:
        print('logging ok')
    else :
        print('logging fail')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    loginform = ui.login.Ui_Form()
    loginform.setupUi(window)
    
    loginform.user_name.setText('j2ee')
    loginform.password.setText('j2ee')
    
    loginform.btn_ok.clicked.connect(btnok_click)
    
    window.show()
    sys.exit(app.exec_())
    