# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : gitControl.py
# @Soft    : tomato_farm
import os
import sys

from PyQt5.QtWidgets import QApplication
from UIImpls.mainWindowImpl import mainWindowImpl

if __name__ == '__main__':
    #界面初始化
    app = QApplication(sys.argv)
    mainWindow = mainWindowImpl()
    type = ''
    if len(sys.argv)>1:
        type = sys.argv[-1]
    mainWindow.showCheck(type)
    sys.exit(app.exec_())
