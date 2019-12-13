# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : gitControl.py
# @Soft    : tomato_farm
import os
import sys
import time

from PyQt5.QtWidgets import QApplication,QDialog
from UIImpls.mainWindowImpl import mainWindowImpl
from UIImpls.unlockDialogImpl import unlockDialogImpl
from util.loadConf import config

if __name__ == '__main__':
    if not os.path.exists("log"):
        os.makedirs("log")
    #界面初始化
    conf = config()
    app = QApplication(sys.argv)
    mainWindow = mainWindowImpl()
    unlockDialog = unlockDialogImpl()
    if conf.decrypt(conf.getOption('LOCK', 'isLock'))=="True":
        if unlockDialog.exec() == QDialog.Accepted:
            mainWindow.show()
        else:
            exit(-1)
    else:
        mainWindow.show()
    sys.exit(app.exec_())
