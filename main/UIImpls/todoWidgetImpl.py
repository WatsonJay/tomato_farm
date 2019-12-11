# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 22:05
# @Author  : Jaywatson
# @File    : todoWidgetImpl.py
# @Soft    : tomato_farm

from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget

from UI.todoWidget import Ui_todoWidget
from UIImpls.noBorderImpl import noBorderImpl

class todoWidgetImpl(QWidget, Ui_todoWidget, noBorderImpl):
    # 初始化
    def __init__(self, parent=None):
        super(todoWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        self.flag = False