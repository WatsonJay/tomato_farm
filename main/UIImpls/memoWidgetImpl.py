# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:34
# @Author  : Jaywatson
# @File    : memoWidgetImpl.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import QWidget

from UI.memoWidget import Ui_memoWidget


class memoWidgetImpl(QWidget, Ui_memoWidget):
    # 初始化
    def __init__(self, parent=None):
        super(memoWidgetImpl, self).__init__(parent)
        self.setupUi(self)