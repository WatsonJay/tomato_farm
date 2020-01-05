# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 17:19
# @Author  : Jaywatson
# @File    : overdueItemImpl.py
# @Soft    : tomato_farm

from PyQt5.QtWidgets import QWidget
from UI.overdueListItem import Ui_overdueListItem

class overdueItemImpl(QWidget, Ui_overdueListItem):
    # 初始化
    def __init__(self, parent=None):
        super(overdueItemImpl, self).__init__(parent)
        self.setupUi(self)

    # 信息填充
    def setInfo(self, data):
        self.taskNameLabel.setText(data['task_name'],"white")