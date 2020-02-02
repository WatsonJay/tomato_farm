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
        self.lineEdit.setVisible(False)
        self.data = {}
        self.title = ""
        self.titleLabel.doubleClicked.connect(self.editTitle)
        self.lineEdit.returnPressed.connect(self.titleSave)

    # 编辑标题
    def editTitle(self):
        self.titleLabel.setVisible(False)
        self.lineEdit.setText(self.titleLabel.text())
        self.lineEdit.setVisible(True)

    # 保存标题
    def titleSave(self):
        self.lineEdit.setVisible(False)
        self.title = self.lineEdit.text()
        self.titleLabel.setText(self.title)
        self.setWindowTitle(self.title)
        self.titleLabel.setVisible(True)