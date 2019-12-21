# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:32
# @Author  : Jaywatson
# @File    : marketWidgetImpl.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import QWidget

from UI.marketWidget import Ui_marketWidget

class marketWidgetImpl(QWidget, Ui_marketWidget):
    # 初始化
    def __init__(self, parent=None):
        super(marketWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        self.deleteWidget.hide()