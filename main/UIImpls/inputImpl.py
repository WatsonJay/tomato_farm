# -*- coding: utf-8 -*-
# @Time    : 2020/1/31 17:25
# @Author  : Jaywatson
# @File    : inputImpl.py
# @Soft    : tomato_farm

from PyQt5.QtWidgets import QDialog
from UI.inputDialog import Ui_Dialog
from UIImpls.noBorderImpl import noBorderImpl
from UIImpls.tipImpl import tipImpl


class inputDialogImpl(QDialog, Ui_Dialog, noBorderImpl, tipImpl):

    # 初始化
    def __init__(self, parent=None):
        super(inputDialogImpl, self).__init__(parent)
        self.setupUi(self)
        self.tiplabel.setVisible(False)
        self.acceptPushButton.clicked.connect(self.sure)
        self.canclePushButton.clicked.connect(self.cancle)
        self.inputLineEdit.textChanged.connect(self.change)

    def change(self):
        if self.inputLineEdit.text() == "":
            self.tiplabel.setVisible(True)
        else:
            self.tiplabel.setVisible(False)

    def sure(self):
        if self.inputLineEdit.text() == "":
            self.tiplabel.setVisible(True)
            return
        else:
            self.accept()
            self.destroy()

    def cancle(self):
        self.reject()
        self.destroy()