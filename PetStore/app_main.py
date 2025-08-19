#coding = utf8

import os
import sys
from PyQt5.QtWidgets import *
import ui.login
from dao.account_dao import AccountBao
import ui.main_window

def btnok_click():
    username = loginform.user_name.text()
    password = loginform.password.text()
    # dao = AccountBao()
    mainwindow.show()
    # account = dao.findbyid(username)
    # if account is not None and account['password'] == password:
    #     print('logging ok')
    #     window.hide()
    #     mainwindow.show()
    # else :
    #     print('logging fail')
    #     QMessageBox.information(window,'登录信息', '登录失败！', QMessageBox.Ok)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    loginform = ui.login.Ui_Form()
    loginform.setupUi(window)
    
    loginform.user_name.setText('j2ee')
    loginform.password.setText('j2ee')
    
    loginform.btn_ok.clicked.connect(btnok_click)
    mainwindow = ui.main_window.MyWindow()
    window.show()
    sys.exit(app.exec_())
    