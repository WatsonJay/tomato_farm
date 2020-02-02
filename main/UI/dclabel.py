# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 14:55
# @Author  : Jaywatson
# @File    : dclabel.py
# @Soft    : tomato_farm
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel


class DCLabel(QLabel):
    doubleClicked = pyqtSignal()

    def __init__(self, parent=None):
        super(DCLabel, self).__init__(parent)

    def mouseDoubleClickEvent(self,e):
        self.doubleClicked.emit()