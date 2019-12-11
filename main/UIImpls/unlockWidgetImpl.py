# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 22:14
# @Author  : Jaywatson
# @File    : unlockWidgetImpl.py
# @Soft    : tomato_farm

import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget

from UI.unlockWidget import Ui_unlockWidget
from UIImpls.noBorderImpl import noBorderImpl

class unlockWidgetImpl(QWidget, Ui_unlockWidget, noBorderImpl):
    # 初始化
    def __init__(self, parent=None):
        super(unlockWidgetImpl, self).__init__(parent)
        self.setupUi(self)