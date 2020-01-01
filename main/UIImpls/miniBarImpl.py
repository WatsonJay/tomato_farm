# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 9:44
# @Author  : Jaywatson
# @File    : miniBarImpl.py
# @Soft    : tomato_farm
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from UI.miniBar import Ui_miniBarForm
from UIImpls.noBorderImpl import noBorderImpl
from UIImpls.tipImpl import tipImpl
from util.loadConf import config
from util.logger import logger


class miniBarImpl(QWidget, Ui_miniBarForm, noBorderImpl, tipImpl):
    # 信号槽
    normalSizeSignal = pyqtSignal()

    # 初始化
    def __init__(self, parent=None):
        super(miniBarImpl, self).__init__(parent)
        self.setupUi(self)
        self.conf = config()
        log = logger()
        self.confmini = log.getlogger('gui')
        self.move(int(self.conf.getOption('miniBar', 'placeX')), int(self.conf.getOption('miniBar', 'placeY')))
        self.taskLabel.setText("无","white")

        self.normalSizeButton.clicked.connect(self.normalSize)


    #切换正常界面
    def normalSize(self):
        self.normalSizeSignal.emit()
        self.conf.addoption('miniBar', 'placeX', str(self.x()))
        self.conf.addoption('miniBar', 'placeY', str(self.y()))

    # 切换迷你界面
    def miniShow(self):
        self.show()

    # 任务进程信息显示
    def taskMsgShow(self, dict):
        self.confmini.debug("status")
