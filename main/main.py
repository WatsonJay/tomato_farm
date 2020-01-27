# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : gitControl.py
# @Soft    : tomato_farm
import os
import sys
import time

from PyQt5.QtWidgets import QApplication
from UIImpls.mainWindowImpl import mainWindowImpl
from util.loadConf import config

if __name__ == '__main__':
    #界面初始化
    conf = config()
    app = QApplication(sys.argv)
    mainWindow = mainWindowImpl()
    mainWindow.showCheck()
    sys.exit(app.exec_())
