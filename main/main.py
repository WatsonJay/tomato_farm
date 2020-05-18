# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : gitControl.py
# @Soft    : tomato_farm
import os
import sys
from util.systemPid import systemPid

from PyQt5.QtWidgets import QApplication
from UIImpls.mainWindowImpl import mainWindowImpl

if __name__ == '__main__':
    systemPid = systemPid()
    if systemPid.check_pid():
        systemPid.write_pid()
        #界面初始化
        app = QApplication(sys.argv)
        mainWindow = mainWindowImpl()
        type = ''
        if len(sys.argv)>1:
            type = sys.argv[-1]
        mainWindow.showCheck(type)
        sys.exit(app.exec_())
