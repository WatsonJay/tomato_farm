# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 22:10
# @Author  : Jaywatson
# @File    : memoViewImpl.py
# @Soft    : tomato_farm

from PyQt5.QtWidgets import QWidget

from UI.memoView import Ui_memoView
from UIImpls.tipImpl import tipImpl


class memoViewImpl(QWidget, Ui_memoView, tipImpl):
    # 初始化
    def __init__(self, parent=None):
        super(memoViewImpl, self).__init__(parent)
        self.setupUi(self)

