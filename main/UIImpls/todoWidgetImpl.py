# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 22:05
# @Author  : Jaywatson
# @File    : todoWidgetImpl.py
# @Soft    : tomato_farm

from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget,QApplication
from UI.todoWidget import Ui_todoWidget
from UIImpls.noBorderImpl import noBorderImpl
from util.loadConf import config
from util.logger import logger


class todoWidgetImpl(QWidget, Ui_todoWidget, noBorderImpl):
    # 初始化
    def __init__(self, parent=None):
        super(todoWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        self.flag = False
        log = logger()
        self.conftodo = log.getlogger('gui')
        self.showHideWidget.setVisible(False)
        self.conf = config()
        self.move(int(self.conf.getOption('todoList', 'placeX')), int(self.conf.getOption('todoList', 'placeY')))
        self.checkHide()

    #鼠标进入事件
    def enterEvent(self, QEvent):
        self.checkShow()

    #鼠标离开事件
    def leaveEvent(self, QEvent):
        self.checkHide()

    #关闭事件
    def closeEvent(self, QCloseEvent):
        widgetGeom = self.geometry()
        self.conf.addoption('todoList', 'placeX', str(widgetGeom.x()))
        self.conf.addoption('todoList', 'placeY', str(widgetGeom.y()))

    #检测隐藏
    def checkHide(self):
        desktop = QApplication.desktop()
        widgetGeom = self.geometry()
        if widgetGeom.x() >= desktop.width() - widgetGeom.width() - 5 and widgetGeom.x() <= desktop.width() - widgetGeom.width() + 5 :
            self.conftodo.debug("鼠标离开,隐藏")
            self.move(desktop.width() - 30, self.y())
            self.showHideWidget.setVisible(True)

    # 检测显示
    def checkShow(self):
        desktop = QApplication.desktop()
        widgetGeom = self.geometry()
        if widgetGeom.x() == desktop.width() - 30 :
            self.conftodo.debug("鼠标进入,显示")
            self.move(desktop.width() - widgetGeom.width(), self.y())
            self.showHideWidget.setVisible(False)