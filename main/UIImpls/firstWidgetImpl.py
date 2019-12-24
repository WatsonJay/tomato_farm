# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:31
# @Author  : Jaywatson
# @File    : firstWidgetImpl.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import QWidget

from UI.firstWidget import Ui_homeWidget
from UIImpls.tipImpl import tipImpl


class firstWidgetImpl(QWidget, Ui_homeWidget, tipImpl):
    # 初始化
    def __init__(self, parent=None):
        super(firstWidgetImpl, self).__init__(parent)
        self.setupUi(self)
