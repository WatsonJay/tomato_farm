# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : mainWindowImpl.py
# @Soft    : tomato_farm
import datetime
import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QCheckBox, QSystemTrayIcon, QMenu, QAction
from UI.mainWindow import Ui_MainWindow
from UIImpls.firstWidgetImpl import firstWidgetImpl
from UIImpls.marketWidgetImpl import marketWidgetImpl
from UIImpls.memoWidgetImpl import memoWidgetImpl
from UIImpls.statisWidgetImpl import statisWidgetImpl
from UIImpls.taskWidgetImpl import taskWidgetImpl
from UIImpls.noBorderImpl import noBorderImpl
from UIImpls.miniBarImpl import miniBarImpl
from UIImpls.tipImpl import tipImpl
from UIImpls.todoWidgetImpl import todoWidgetImpl
from util.loadData import sqlite
import UI.icons_rc



class mainWindowImpl(QMainWindow, Ui_MainWindow, noBorderImpl, tipImpl):
    #信号槽
    miniSizeSignal = pyqtSignal()
    # 初始化
    def __init__(self, parent=None):
        super(mainWindowImpl, self).__init__(parent)
        self.setupUi(self)
        self.closeNow = True
        self.miniBar = miniBarImpl()
        self.todolist = todoWidgetImpl()
        self.todolist.show()
        self.trayIcon()
        #添加功能页面
        firstWidget = firstWidgetImpl()
        statisWidget = statisWidgetImpl()
        taskWidget = taskWidgetImpl()
        memoWidget = memoWidgetImpl()
        marketWidget = marketWidgetImpl()
        self.stackedWidget.addWidget(firstWidget)
        self.stackedWidget.addWidget(statisWidget)
        self.stackedWidget.addWidget(taskWidget)
        self.stackedWidget.addWidget(memoWidget)
        self.stackedWidget.addWidget(marketWidget)
        self.firstPageButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.statisButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.taskButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.memoButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.marketButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.miniSizeButton.clicked.connect(self.miniSize)
        self.miniSizeSignal.connect(self.miniBar.miniShow)  # 通过信号槽设置时间
        self.miniBar.normalSizeSignal.connect(self.normalShow)

    #切换迷你界面
    def miniSize(self):
        self.miniSizeSignal.emit()
        self.hide()

    #切换正常界面
    def normalShow(self):
        self.miniBar.hide()
        self.show()

    #托盘事件
    def trayIcon(self):
        self.mSysTrayIcon = QSystemTrayIcon(self)
        trayIcon = QIcon()
        trayIcon.addPixmap(QPixmap(":/icon/tomato.png"), QIcon.Normal, QIcon.Off)
        self.mSysTrayIcon.setIcon(trayIcon)
        self.mSysTrayIcon.setToolTip("番茄农场")
        self.mSysTrayIcon.activated.connect(self.normalShow)
        tpMenu = QMenu()
        restoreAction = QAction('还原', self, triggered=self.show)  # 添加一级菜单动作选项(还原主窗口)
        quitAction = QAction('退出', self, triggered=self.closeWithout)  # 添加一级菜单动作选项(退出程序)
        tpMenu.addAction(restoreAction)
        tpMenu.addAction(quitAction)
        self.mSysTrayIcon.setContextMenu(tpMenu)
        self.mSysTrayIcon.show()

    #检查任务逾期
    def checkOverdue(self):
        sqliteI = sqlite('./config/tomato.db')
        now = datetime.date.today().strftime('%Y-%m-%d')
        sql = "Update t_base_task SET is_overdue = ? where deadline_time < ?"
        sqliteI.execute(sql, [1,now])

    # 重写打开事件
    def show(self):
        super(mainWindowImpl, self).show()
        self.checkOverdue()
        return self

    # 立刻关闭
    def closeWithout(self):
        self.closeNow = False
        self.todolist.close()
        self.mSysTrayIcon.hide()
        self.close()

    #重写关闭事件
    def closeEvent(self, event):
        if self.closeNow:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('番茄农场')
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText('将要关闭软件')
            msgBox.setInformativeText('是否最小化到托盘?')
            yes = msgBox.addButton('最小化到托盘', QMessageBox.YesRole)
            no = msgBox.addButton('关闭', QMessageBox.NoRole)
            msgBox.setDefaultButton(yes)
            cb = QCheckBox('不再显示该提示')
            msgBox.setCheckBox(cb)
            reply = msgBox.exec()
            if reply == 0:
                event.ignore()
                self.hide()
            else:
                self.todolist.close()
                event.accept()
                self.mSysTrayIcon.hide()

