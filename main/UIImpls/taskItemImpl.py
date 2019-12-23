# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 12:19
# @Author  : Jaywatson
# @File    : taskItemImpl.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import QWidget

from UI.taskItem import Ui_taskItem

class taskItemImpl(QWidget, Ui_taskItem):
    # 初始化
    def __init__(self, parent=None):
        super(taskItemImpl, self).__init__(parent)
        self.setupUi(self)
        self.taskId = ''
        self.taskTitle = ''