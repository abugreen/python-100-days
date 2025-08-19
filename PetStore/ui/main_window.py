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
        
        # go_btn.clicked.connect(self.go_btnclick)
        # rest_btn.clicked.connect(self.rest_btnclick)
        self.table = self.create_table()
        main_layout.addLayout(top_layout)
        
        # 创建分割窗口
        splitter = QSplitter()
        splitter.setSizes([900, 300])
        # 把表格添加到分割窗口
        splitter.addWidget(self.table)
        
        
    # 创建表格对象
    def create_table(self):

        # 创建表格
        table = QTableWidget()
        # 设置表格行数
        table.setRowCount(len(self.datas))
        # 设置表格列数
        table.setColumnCount(len(column_names))
        # 设置表格字体
        table.setFont(QFont("微软雅黑", 10))
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
        horizontalHeader.setFont(QFont("微软雅黑", 10))
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
        
        