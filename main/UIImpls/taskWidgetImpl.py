# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:36
# @Author  : Jaywatson
# @File    : taskWidgetImpl.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import QWidget

from UI.taskWidget import Ui_taskWidget

class taskWidgetImpl(QWidget, Ui_taskWidget):
    # 初始化
    def __init__(self, parent=None):
        super(taskWidgetImpl, self).__init__(parent)
        self.setupUi(self)