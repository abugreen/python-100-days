from PyQt6.QtWidgets import QWidget,QApplication,QDialog , QMessageBox
import sys
from Ui_password_gen import Ui_PasswordGenerate
import string
import random

class MyPasswordGenerate(Ui_PasswordGenerate,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.pushButton.clicked.connect(self.new_password)
        
    def new_password(self):
        site = self.lineEdit_site.text()
        if not site:
            QMessageBox.warning(self, "訊息提示" , "請輸入site")
            return
        
        words = []
        if self.checkBox_upper.isChecked():
            words.append(string.ascii_uppercase * 2)
            
        if self.checkBox_lower.isChecked():
            words.append(string.ascii_lowercase * 2)
            
        if self.checkBox_number.isChecked():
            words.append(string.digits * 2)
        
        if self.checkBox_puc.isChecked():
            words.append(string.punctuation * 2)
        
        if not words:
            words = (string.digits 
                    + string.ascii_uppercase 
                    + string.ascii_lowercase 
                    + string.punctuation)  
        else:
            words = "".join(words)
        
        words = random.sample(list(words), 20)
        password = "".join(words)
       
        self.lineEdit_result.setText(password)
        QMessageBox.information(
            self , "訊息提示" , "密碼生成成功")
        
        with open("我的密碼本", "a", encoding="utf-8") as f:
            f.write(f"{site}\t{password}\n")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myPasswordGernerate = MyPasswordGenerate()
    sys.exit(app.exec())
    