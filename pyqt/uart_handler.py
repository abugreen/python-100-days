import serial
import serial.tools.list_ports
from PyQt5.QtCore import QThread, pyqtSignal

class UARTHandler(QThread):
    """處理 UART 通訊的類別"""
    data_received = pyqtSignal(str)  # 用於發送接收到的數據
    error_occurred = pyqtSignal(str)  # 用於發送錯誤訊息

    def __init__(self):
        super().__init__()
        self.serial_port = None
        self.is_running = False

    @staticmethod
    def get_available_ports():
        """獲取可用的串口列表"""
        return [port.device for port in serial.tools.list_ports.comports()]

    def connect(self, port, baudrate):
        """連接到指定的串口"""
        try:
            self.serial_port = serial.Serial(
                port=port,
                baudrate=baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=1
            )
            self.is_running = True
            self.start()  # 啟動執行緒
            return True
        except serial.SerialException as e:
            self.error_occurred.emit(f"串口連接錯誤: {str(e)}")
            return False

    def stop_connection(self):
        """中斷串口連接"""
        self.is_running = False
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
        return True

    def run(self):
        """執行緒主循環，持續讀取串口數據"""
        while self.is_running:
            try:
                if self.serial_port and self.serial_port.is_open:
                    if self.serial_port.in_waiting:
                        data = self.serial_port.readline().decode('utf-8').strip()
                        if data:  # 確保數據不為空
                            self.data_received.emit(data)
            except serial.SerialException as e:
                self.error_occurred.emit(f"串口讀取錯誤: {str(e)}")
                self.stop_connection()
                break
            except Exception as e:
                self.error_occurred.emit(f"未知錯誤: {str(e)}")
                self.disconnect()
                break

    def __del__(self):
        """確保在物件銷毀時關閉串口"""
        self.disconnect()