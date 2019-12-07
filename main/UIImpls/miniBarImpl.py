# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 9:44
# @Author  : Jaywatson
# @File    : miniBarImpl.py
# @Soft    : tomato_farm

from PyQt5.QtWidgets import QWidget
from UI.miniBar import Ui_miniBarForm

class miniBarImpl(QWidget, Ui_miniBarForm):
    # 初始化
    def __init__(self, parent=None):
        super(miniBarImpl, self).__init__(parent)
        self.setupUi(self)