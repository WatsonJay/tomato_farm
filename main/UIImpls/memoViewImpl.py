# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 22:10
# @Author  : Jaywatson
# @File    : memoViewImpl.py
# @Soft    : tomato_farm
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox

from UI.memoView import Ui_memoView
from UIImpls.tipImpl import tipImpl


class memoViewImpl(QWidget, Ui_memoView, tipImpl):
    # 信号槽
    closeSignal = pyqtSignal()
    titleChangeSignal = pyqtSignal(str,str)

    # 初始化
    def __init__(self, parent=None):
        super(memoViewImpl, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setVisible(False)
        self.data = {}
        self.title = ""
        self.edited = False
        self.textEdit.document().setModified(False)
        self.tempKeyWord = ""
        self.titleLabel.doubleClicked.connect(self.editTitle)
        self.lineEdit.returnPressed.connect(self.titleSave)

    # 编辑标题
    def editTitle(self):
        self.titleLabel.setVisible(False)
        self.lineEdit.setText(self.titleLabel.text())
        self.lineEdit.setVisible(True)
        self.edited = True

    def isModified(self):
        return self.textEdit.document().isModified() or self.edited

    # 保存标题
    def titleSave(self):
        self.lineEdit.setVisible(False)
        self.title = self.lineEdit.text()
        self.titleLabel.setText(self.title)
        self.setWindowTitle(self.title)
        self.data['node_name'] = self.title
        self.titleLabel.setVisible(True)
        self.titleChangeSignal.emit(self.data['id'],self.title)

    def closeEvent(self, event):
        if self.isModified():
            msgBox = QMessageBox()
            msgBox.setWindowTitle('保存')
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setInformativeText("是否保存对'{0}'的修改?".format(self.title))
            yes = msgBox.addButton('是', QMessageBox.YesRole)
            no = msgBox.addButton('否', QMessageBox.NoRole)
            cancle = msgBox.addButton('取消', QMessageBox.RejectRole)
            msgBox.setDefaultButton(yes)
            reply = msgBox.exec()
            if reply == 0:
                self.closeSignal.emit()
            if reply == 1:
                self.close()
            else:
                event.ignore()