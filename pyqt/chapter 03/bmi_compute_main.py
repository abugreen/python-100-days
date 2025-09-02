from PyQt6.QtWidgets import QApplication,QDialog
from Ui_bmi_compute import Ui_BMI_compute
import sys


class MyBmiCompute(Ui_BMI_compute ,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.pushButton.clicked.connect(self.compute_bmi)
        
    def compute_bmi(self):
        pass
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mybmicompute = MyBmiCompute()
    
    sys.exit(app.exec())