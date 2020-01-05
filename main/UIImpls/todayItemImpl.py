# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 17:20
# @Author  : Jaywatson
# @File    : todayItemImpl.py
# @Soft    : tomato_farm

from PyQt5.QtWidgets import QWidget
from UI.todayListItem import Ui_todayListItem

class todayItemImpl(QWidget, Ui_todayListItem):
    # 初始化
    def __init__(self, parent=None):
        super(todayItemImpl, self).__init__(parent)
        self.setupUi(self)

    # 信息填充
    def setInfo(self, data):
        self.taskNameLabel.setText(data['task_name'],"white")