# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 22:05
# @Author  : Jaywatson
# @File    : todoWidgetImpl.py
# @Soft    : tomato_farm
import datetime

from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QListWidgetItem
from UI.todoWidget import Ui_todoWidget
import UI.icons_rc
from UIImpls.noBorderImpl import noBorderImpl
from UIImpls.overdueItemImpl import overdueItemImpl
from UIImpls.todayItemImpl import todayItemImpl
from util.loadConf import config
from util.loadData import sqlite
from util.logger import logger


class todoWidgetImpl(QWidget, Ui_todoWidget, noBorderImpl):
    # 信号槽
    taskRefreshSignal = pyqtSignal()

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
        self.sqlite = sqlite('./config/tomato.db')
        self.move(int(self.conf.getOption('todoList', 'placeX')), int(self.conf.getOption('todoList', 'placeY')))
        self.lockButton.clicked.connect(self.lockStatus) #锁定/解锁
        self.changeButton.clicked.connect(self.changeCurrentPage) #切换当前页面

    #重定义展示
    def show(self):
        super(todoWidgetImpl, self).show()
        self.checkHide()
        return self

    #全部刷新
    def refreshAll(self):
        self.loadTodayTask()
        self.loadOverdueTask()

    #今日列表刷新
    def loadTodayTask(self):
        self.todayListWidget.clear()
        now = str(datetime.date.today())
        try:
            sql = '''select tbt.id, tbt.task_name, tbt.task_during, ttld.is_doing, ttld.is_top from t_base_task tbt
                  join t_task_link_date ttld on tbt.id = ttld.task_id
                  where tbt.is_dated = ? and tbt.is_overdue = ? and tbt.is_finish = ? and ttld.link_date = ? order by ttld.is_top DESC'''
            datas = self.sqlite.executeQuery(sql, 1, 0, 0, now)
            for data in datas:
                taskItem, ListItem = self.makeTodayItem(data)
                self.todayListWidget.addItem(ListItem)
                self.todayListWidget.setItemWidget(ListItem, taskItem)
                taskItem.taskRefreshSignal.connect(self.refreshAll)
        except Exception as e:
            self.conffirst.error(e)

    #逾期列表刷新
    def loadOverdueTask(self):
        self.overdueListWidget.clear()
        try:
            sql = '''select tbt.id, tbt.task_name, tbt.task_during, ttld.is_doing,ttld.link_date from t_base_task tbt
                  join t_task_link_date ttld on tbt.id = ttld.task_id
                  where tbt.is_dated = ? and tbt.is_overdue = ? and tbt.is_finish = ? order by ttld.link_date DESC'''
            datas = self.sqlite.executeQuery(sql, 1, 1, 0)
            for data in datas:
                taskItem, ListItem = self.makeOverdueItem(data)
                self.overdueListWidget.addItem(ListItem)
                self.overdueListWidget.setItemWidget(ListItem, taskItem)
        except Exception as e:
            self.conftodo.error(e)

    # 创建列表项
    def makeOverdueItem(self, data):
        firstItem = overdueItemImpl()
        firstItem.setInfo(data)
        listItem = QListWidgetItem()
        listItem.setSizeHint(firstItem.size())
        return firstItem, listItem

    def makeTodayItem(self, data):
        firstItem = todayItemImpl()
        firstItem.setInfo(data)
        listItem = QListWidgetItem()
        listItem.setSizeHint(firstItem.size())
        return firstItem, listItem

    # 锁定检查
    def checkLock(self):
        icon = QtGui.QIcon()
        if self.conf.getOption('todoList', 'unlock') == False:
            self.unLock = False
            icon.addPixmap(QtGui.QPixmap(":/icon/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            self.unLock = True
            icon.addPixmap(QtGui.QPixmap(":/icon/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lockButton.setIcon(icon)

    # 锁定/解锁
    def lockStatus(self):
        icon = QtGui.QIcon()
        if self.unLock == True:
            self.unLock = False
            icon.addPixmap(QtGui.QPixmap(":/icon/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            self.unLock = True
            icon.addPixmap(QtGui.QPixmap(":/icon/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lockButton.setIcon(icon)

    # 页面切换
    def changeCurrentPage(self):
        if self.currentLabel.text() == 'Today':
            self.currentLabel.setText('Overdue')
            self.changeButton.setText('Today')
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.currentLabel.setText('Today')
            self.changeButton.setText('Overdue')
            self.stackedWidget.setCurrentIndex(0)

    #检测隐藏
    def checkHide(self):
        desktop = QApplication.desktop()
        current_monitor = desktop.screenNumber(self)
        desktopGem = desktop.screenGeometry(current_monitor)
        widgetGeom = self.geometry()
        if widgetGeom.x() >= desktopGem.x() + desktopGem.width() - widgetGeom.width() - 5 and widgetGeom.x() <= desktopGem.x() + desktopGem.width() :
            self.conftodo.debug("鼠标离开,隐藏")
            self.showHideWidget.setVisible(True)
            self.move(desktopGem.x() + desktopGem.width() - self.showHideWidget.width() - self.mainWidget.width()//2, self.y())
            self.mainWidget.setVisible(False)

    # 检测显示
    def checkShow(self):
        desktop = QApplication.desktop()
        current_monitor = desktop.screenNumber(self)
        desktopGem = desktop.screenGeometry(current_monitor)
        widgetGeom = self.geometry()
        if widgetGeom.x() == desktopGem.x() + desktopGem.width() - self.showHideWidget.width() - self.mainWidget.width()//2:
            self.conftodo.debug("鼠标进入,显示")
            self.mainWidget.setVisible(True)
            self.move(desktopGem.x() +desktopGem.width() - widgetGeom.width(), self.y())
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