from PyQt5.QtWidgets import *
import sys


class Empyt_ui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("empty window")
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Empyt_ui()
    window.show()
    
    sys.exit(app.exec_())
        