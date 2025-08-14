import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QLabel, QPushButton, QSpinBox, QComboBox,
                           QMessageBox)
from PyQt5.QtGui import QPainter, QPen, QColor, QCloseEvent
from PyQt5.QtCore import Qt, QSize, QPoint
from uart_handler import UARTHandler

# 顏色常數
COLOR_MAP = {
    '黑色': QColor(0, 0, 0),
    '紅色': QColor(255, 0, 0),
    '藍色': QColor(0, 0, 255),
    '綠色': QColor(0, 255, 0)
}

class DrawingBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uart = UARTHandler()
        self.canvas = None  # 先初始化為 None
        self.coord_label = None  # 初始化座標標籤
        self.initUI()
        # 在 UI 初始化後再連接信號
        self.uart.data_received.connect(self.handle_uart_data)
        self.uart.error_occurred.connect(self.handle_uart_error)
        
    def initUI(self):
        # 設定主視窗
        self.setWindowTitle('Arduino 畫板')
        self.setFixedSize(1000, 700)  # 設定視窗大小（包含控制面板區域）
        
        # 建立中央元件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 建立主要布局
        main_layout = QHBoxLayout(central_widget)
        
        # 建立控制面板
        control_panel = self.createControlPanel()
        main_layout.addLayout(control_panel)
        
        # 建立畫布區域
        self.canvas = Canvas()
        main_layout.addWidget(self.canvas)
        
        # 連接顏色和粗細變更事件（在控制面板創建後）
        self.color_combo.currentTextChanged.connect(self.update_pen_color)
        self.thickness_spin.valueChanged.connect(self.update_pen_thickness)
        
        # 顯示視窗
        self.show()
        
    def createControlPanel(self):
        control_layout = QVBoxLayout()
        
        # 串口設定區域
        uart_group = QWidget()
        uart_layout = QVBoxLayout(uart_group)
        uart_layout.addWidget(QLabel('串口設定'))
        
        # 串口選擇
        self.port_combo = QComboBox()
        uart_layout.addWidget(self.port_combo)
        
        # 鮑率選擇
        baud_layout = QHBoxLayout()
        baud_layout.addWidget(QLabel('鮑率：'))
        self.baud_combo = QComboBox()
        self.baud_combo.addItems(['9600', '19200', '38400', '115200'])
        baud_layout.addWidget(self.baud_combo)
        uart_layout.addLayout(baud_layout)
        
        # 更新串口列表
        self.port_combo.addItems(UARTHandler.get_available_ports())
        
        # 連接按鈕
        self.connect_btn = QPushButton('連接')
        self.connect_btn.clicked.connect(self.toggle_connection)
        uart_layout.addWidget(self.connect_btn)
        
        control_layout.addWidget(uart_group)
        
        # 畫筆設定區域
        pen_group = QWidget()
        pen_layout = QVBoxLayout(pen_group)
        pen_layout.addWidget(QLabel('畫筆設定'))
        
        # 顏色選擇
        self.color_combo = QComboBox()
        self.color_combo.addItems(['黑色', '紅色', '藍色', '綠色'])
        pen_layout.addWidget(self.color_combo)
        
        # 粗細設定
        thickness_layout = QHBoxLayout()
        thickness_layout.addWidget(QLabel('粗細：'))
        self.thickness_spin = QSpinBox()
        self.thickness_spin.setRange(1, 20)
        self.thickness_spin.setValue(2)
        thickness_layout.addWidget(self.thickness_spin)
        pen_layout.addLayout(thickness_layout)
        
        control_layout.addWidget(pen_group)
        
        # 座標顯示區域
        coord_group = QWidget()
        coord_layout = QVBoxLayout(coord_group)
        coord_layout.addWidget(QLabel('座標資訊'))
        self.coord_label = QLabel('X: 0, Y: 0')
        coord_layout.addWidget(self.coord_label)
        
        control_layout.addWidget(coord_group)
        
        # 添加彈性空間
        control_layout.addStretch()
        
        return control_layout
    
    def handle_uart_data(self, data):
        """處理接收到的 UART 數據"""
        try:
            # 解析 x,y 座標
            x, y = map(int, data.split(','))
            
            # 更新座標顯示
            if self.coord_label:
                self.coord_label.setText(f'X: {x}, Y: {y}')
            
            # 在畫布上添加點
            if self.canvas:
                self.canvas.add_point(x, y)
        except ValueError as e:
            self.handle_uart_error(f"數據格式錯誤: {data}")
    
    def handle_uart_error(self, error_msg):
        """處理 UART 錯誤"""
        QMessageBox.warning(self, '錯誤', error_msg)
    
    def toggle_connection(self):
        """切換串口連接狀態"""
        if self.connect_btn.text() == '連接':
            port = self.port_combo.currentText()
            baudrate = int(self.baud_combo.currentText())
            
            if self.uart.connect(port, baudrate):
                self.connect_btn.setText('中斷連接')
                self.port_combo.setEnabled(False)
                self.baud_combo.setEnabled(False)
        else:
            self.uart.stop_connection()
            self.connect_btn.setText('連接')
            self.port_combo.setEnabled(True)
            self.baud_combo.setEnabled(True)
    
    def update_pen_color(self, color_name: str):
        """更新畫筆顏色"""
        if self.canvas:
            self.canvas.pen_color = COLOR_MAP[color_name]
    
    def update_pen_thickness(self, thickness: int):
        """更新畫筆粗細"""
        if self.canvas:
            self.canvas.pen_thickness = thickness
    
    def closeEvent(self, a0: QCloseEvent | None) -> None:
        """關閉視窗時停止 UART 連接"""
        self.uart.stop_connection()
        if a0 is not None:
            a0.accept()

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 設定畫布大小和背景
        self.setFixedSize(800, 600)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(palette)
        
        # 初始化繪圖參數
        self.points = []
        self.pen_color = QColor(0, 0, 0)  # 黑色
        self.pen_thickness = 2
        
    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 設定畫筆
        pen = QPen(self.pen_color, self.pen_thickness)
        painter.setPen(pen)
        
        # 繪製線條
        if len(self.points) > 1:
            for i in range(len(self.points) - 1):
                painter.drawLine(self.points[i], self.points[i + 1])
                
    def add_point(self, x, y):
        """添加新的座標點"""
        self.points.append(QPoint(x, y))
        self.update()  # 觸發重繪

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawingBoard()
    sys.exit(app.exec_())