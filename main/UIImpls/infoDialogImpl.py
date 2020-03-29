# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 19:35
# @Author  : Jaywatson
# @File    : infoDialogImpl.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import QDialog

from UI.infoDialog import Ui_InfoDialog
from UIImpls.noBorderImpl import noBorderImpl


class infoDialogImpl(QDialog, Ui_InfoDialog, noBorderImpl):

    # 初始化
    def __init__(self, parent=None):
        super(infoDialogImpl, self).__init__(parent)
        self.setupUi(self)
        self.infoPushButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.funcPushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.publisnPushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))