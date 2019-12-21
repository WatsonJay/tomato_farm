# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:34
# @Author  : Jaywatson
# @File    : statisWidgetImpl.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import QWidget

from UI.statisWidget import Ui_statisWidget

class statisWidgetImpl(QWidget, Ui_statisWidget):
    # 初始化
    def __init__(self, parent=None):
        super(statisWidgetImpl, self).__init__(parent)
        self.setupUi(self)