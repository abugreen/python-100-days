from PyQt6.QtWidgets import QWidget,QApplication,QDialog
import sys
from password_gen import Ui_PasswordGenerate

class MyPasswordGenerate(Ui_PasswordGenerate,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myPasswordGernerate = MyPasswordGenerate()
    sys.exit(app.exec())
    