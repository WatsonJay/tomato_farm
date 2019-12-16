# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 22:05
# @Author  : Jaywatson
# @File    : todoWidgetImpl.py
# @Soft    : tomato_farm

from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from UI.todoWidget import Ui_todoWidget
import UI.icons_rc
from util.loadConf import config
from util.logger import logger


class todoWidgetImpl(QWidget, Ui_todoWidget):
    # 初始化
    def __init__(self, parent=None):
        super(todoWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        self.flag = False
        self.mouseflag = False
        log = logger()
        self.conftodo = log.getlogger('gui')
        self.showHideWidget.setVisible(False)
        self.conf = config()
        self.checkLock()
        self.move(int(self.conf.getOption('todoList', 'placeX')), int(self.conf.getOption('todoList', 'placeY')))
        self.checkHide()
        self.lockButton.clicked.connect(self.lockStatus) #锁定/解锁
        self.changeButton.clicked.connect(self.changeCurrentPage) #切换当前页面

    #锁定检查
    def checkLock(self):
        icon = QtGui.QIcon()
        if self.conf.getOption('todoList', 'unlock') == False:
            self.unLock = False
            icon.addPixmap(QtGui.QPixmap(":/icon/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            self.unLock = True
            icon.addPixmap(QtGui.QPixmap(":/icon/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lockButton.setIcon(icon)

    #锁定/解锁
    def lockStatus(self):
        icon = QtGui.QIcon()
        if self.unLock == True:
            self.unLock = False
            icon.addPixmap(QtGui.QPixmap(":/icon/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            self.unLock = True
            icon.addPixmap(QtGui.QPixmap(":/icon/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lockButton.setIcon(icon)

    def changeCurrentPage(self):
        if self.currentLabel.text() == 'Today':
            self.currentLabel.setText('Overdue')
            self.changeButton.setText('Today')
        else:
            self.currentLabel.setText('Today')
            self.changeButton.setText('Overdue')
    #检测隐藏
    def checkHide(self):
        desktop = QApplication.desktop()
        widgetGeom = self.geometry()
        if widgetGeom.x() >= desktop.width() - widgetGeom.width() - 5 :
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

    # 鼠标进入事件
    def enterEvent(self, QEvent):
        self.checkShow()

    # 鼠标离开事件
    def leaveEvent(self, QEvent):
        self.checkHide()

    # 关闭事件
    def closeEvent(self, QCloseEvent):
        widgetGeom = self.geometry()
        self.conf.addoption('todoList', 'placeX', str(widgetGeom.x()))
        self.conf.addoption('todoList', 'placeY', str(widgetGeom.y()))

    #无边框窗体移动
    def mousePressEvent(self, QMouseEvent):
        try:
            if QMouseEvent.button() == QtCore.Qt.LeftButton and self.unLock:
                self.mouseflag = True
                self.m_Position = QMouseEvent.globalPos() - self.pos()
                QMouseEvent.accept()
                self.setCusor(QCursor(QtCore.Qt.OpenHandCursor))
        except Exception as e:
            pass

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.mouseflag and self.unLock:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.mouseflag = False
        self.setCursor(QCursor(QtCore.Qt.ArrowCursor))

    # 提示窗口
    def Tips(self, message):
        QMessageBox.about(self, "提示", message)