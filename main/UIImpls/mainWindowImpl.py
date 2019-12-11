# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : mainWindowImpl.py
# @Soft    : tomato_farm
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow

from UI.mainWindow import Ui_MainWindow
from UIImpls.noBorderImpl import noBorderImpl

class mainWindowImpl(QMainWindow, Ui_MainWindow, noBorderImpl):
    # 初始化
    def __init__(self, parent=None):
        super(mainWindowImpl, self).__init__(parent)
        self.setupUi(self)

