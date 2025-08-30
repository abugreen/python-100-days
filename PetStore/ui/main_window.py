# coding=utf-8

import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import *

from dao.product_dao import ProductDao

column_names = ['商品编号', '商品类别', '商品中文名', '商品英文名']

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        dao = ProductDao()
        self.datas = dao.findall()
        
        self.initUI()
        
    def initUI(self):
        self.resize(1000 , 700)
        self.setWindowTitle('宠物商品列表')
        
        main_layout = QVBoxLayout(self)
        top_layout = QHBoxLayout()
        label = QLabel("选中商品类别：")
        self.combo_box = QComboBox()
        self.combo_box.addItems(['所有类别', '鱼类', '犬类', '爬行类', '猫类', '鸟类'])
        rest_btn = QPushButton('重置')
        go_btn = QPushButton('查询')
        # 把控件添加到top_layout
        top_layout.addWidget(label)
        top_layout.addWidget(self.combo_box)
        top_layout.addWidget(rest_btn)
        top_layout.addWidget(go_btn)
        main_layout.addLayout(top_layout)
        # go_btn.clicked.connect(self.go_btnclick)
        # rest_btn.clicked.connect(self.rest_btnclick)
        self.table = self.create_table()
       
        # 创建分割窗口
        splitter = QSplitter()
        splitter.setSizes([900, 300])
        # 把表格添加到分割窗口
        splitter.addWidget(self.table)
        main_layout.addWidget(splitter)
        
        # 详细面板
        detail_panel = QWidget()
        # 详细布局管理器
        layout = QVBoxLayout()
        # 是设置详细面板布局管理器
        detail_panel.setLayout(layout)
        # 商品图标
        self.imagelabel = QLabel()
        # 商品详细标签
        self.desc_label = QLabel()
        self.desc_label.setWordWrap(True)

        self.price_label = QLabel()
        # 商品单价标签
        self.cost_label = QLabel()

        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)

        line2 = QFrame()
        line2.setFrameShape(QFrame.HLine)
        line2.setFrameShadow(QFrame.Sunken)

        # 把控件添加到layout
        layout.addWidget(self.imagelabel)
        # 把分隔休线添加到详细面板
        layout.addWidget(line1)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.price_label)
        layout.addWidget(self.cost_label)

        # 把分隔休线添加到详细面板
        layout.addWidget(line2)

        layout.addStretch()
        layout.addWidget(QPushButton('添加购物车'))
        layout.addWidget(QPushButton('查看购物车'))

        splitter.addWidget(detail_panel)
        # 将表格放到布局管理器中
        # main_layout.addWidget(table)
        # 将隔窗口添加到main_layout
        main_layout.addWidget(splitter)
        
    # 创建表格对象
    def create_table(self):

        # 创建表格
        table = QTableWidget()
        # 设置表格行数
        table.setRowCount(len(self.datas))
        # 设置表格列数
        table.setColumnCount(len(column_names))
        # 设置表格字体
        #table.setFont(QFont("微软雅黑", 10))
        # 设置表格禁止编辑
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格列标签
        table.setHorizontalHeaderLabels(column_names)
        # 获得列视图
        horizontalHeader = table.horizontalHeader()
        # 设置表格列宽根据内容自适
        horizontalHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        # 获得行视图
        verticalHeader = table.horizontalHeader()
        # 设置表格行高根据内容自适应
        verticalHeader.setSectionResizeMode(QHeaderView.ResizeToContents)
        #   设置表格列标签字体
        #horizontalHeader.setFont(QFont("微软雅黑", 10))
        # 设置表格选择行为，SelectRows为行选择模式。
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 设置表格数据
        for row, dict in enumerate(self.datas):
            table.setItem(row, 0, QTableWidgetItem(dict['productid']))
            table.setItem(row, 1, QTableWidgetItem(dict['category']))
            table.setItem(row, 2, QTableWidgetItem(dict['cname']))
            table.setItem(row, 3, QTableWidgetItem(dict['ename']))

            # 选择表格行信号到select_row槽函数
            table.itemSelectionChanged.connect(self.select_row)
            # 槽函数

        return table
    
    def select_row(self):
        """ 选择表格行变化 """
        table = self.sender()
        selectedRowNo = self.table.currentRow()  # 获得选中行号
        # 获得选中行数据
        dict = self.datas[selectedRowNo]
        # 更新详细面板

        # 图片文件路径
        filename = dict['image']
        # 获得当前文件的绝对路径
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        # 图片的完整路径
        f = os.path.join(curr_dir, 'images', filename)
        # QT图片对象
        pixmap = QPixmap(f)
        # 设置标签
        self.imagelabel.setPixmap(pixmap)
        self.desc_label.setText('商品描述：' + dict['descn'])
        self.price_label.setText('商品市场价：{0:.2f}'.format(dict['listprice']))
        self.cost_label.setText('商品单价：：{0:.2f}'.format(dict['unitcost']))

        
        