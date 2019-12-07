# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : gitControl.py
# @Soft    : tomato_farm
import os
import sys

from PyQt5.QtWidgets import QApplication
#from UIImpls.mainWindowImpl import mainWindowImpl
from UIImpls.todoWidgetImpl import todoWidgetImpl

if __name__ == '__main__':
    if not os.path.exists("log"):
        os.makedirs("log")
    #界面初始化
    app = QApplication(sys.argv)
    mainWindow = todoWidgetImpl()
    mainWindow.show()
    sys.exit(app.exec_())