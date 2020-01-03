# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : mainWindowImpl.py
# @Soft    : tomato_farm
import datetime
import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QCheckBox, QSystemTrayIcon, QMenu, QAction
from UI.mainWindow import Ui_MainWindow
from UIImpls.firstWidgetImpl import firstWidgetImpl
from UIImpls.marketWidgetImpl import marketWidgetImpl
from UIImpls.memoWidgetImpl import memoWidgetImpl
from UIImpls.messageWidgetImpl import messageWidgetImpl
from UIImpls.statisWidgetImpl import statisWidgetImpl
from UIImpls.taskWidgetImpl import taskWidgetImpl
from UIImpls.noBorderImpl import noBorderImpl
from UIImpls.miniBarImpl import miniBarImpl
from UIImpls.tipImpl import tipImpl
from UIImpls.todoWidgetImpl import todoWidgetImpl
from util.loadData import sqlite
import UI.icons_rc
from util.logger import logger


class mainWindowImpl(QMainWindow, Ui_MainWindow, noBorderImpl, tipImpl):
    #信号槽
    miniSizeSignal = pyqtSignal()
    taskRefreshSignal = pyqtSignal()
    taskCheckSignal = pyqtSignal(bool)
    # 初始化
    def __init__(self, parent=None):
        super(mainWindowImpl, self).__init__(parent)
        self.setupUi(self)
        self.closeNow = True
        self.task = {}
        log = logger()
        self.confmain = log.getlogger('gui')
        self.trayIcon()
        self.checkOverdue()
        #界面初始化
        self.timer = QTimer()
        self.miniBar = miniBarImpl()
        self.todolist = todoWidgetImpl()
        self.messageView = messageWidgetImpl()
        self.todolist.show()
        self.taskTitleLabel.setText("无")
        self.readyTomatoLabel.setText("0")
        self.totalTomatoLabel.setText("0")
        self.timeLcd.display("00:00")
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

        #信号绑定
        self.taskRefreshSignal.connect(firstWidget.refreshAll)
        self.taskRefreshSignal.connect(taskWidget.refreshAll)
        self.miniSizeSignal.connect(self.miniBar.miniShow)
        self.taskCheckSignal.connect(firstWidget.taskCheck)
        firstWidget.taskRefreshSignal.connect(taskWidget.refreshAll)
        taskWidget.taskRefreshSignal.connect(firstWidget.refreshAll)
        firstWidget.taskStartSignal.connect(self.taskStart)

        #功能绑定
        self.firstPageButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.statisButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.taskButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.memoButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.marketButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.miniSizeButton.clicked.connect(self.miniSize)
        self.miniBar.normalSizeSignal.connect(self.normalShow)
        self.timer.timeout.connect(self.taskStageShow)

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
        try:
            sqliteI = sqlite('./config/tomato.db')
            now = datetime.date.today().strftime('%Y-%m-%d')
            sql = '''Update t_base_task
                  SET is_overdue = ? 
                  where is_finish = ? and id in (select task_id from t_task_link_date where link_date < ?)'''
            sqliteI.execute(sql, [1, 0, now])
            self.taskRefreshSignal.emit()
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmain.error(e)

    #启动任务线程
    def taskStart(self,dict):
        if self.task != {}:
            reply = QMessageBox.question(self, '任务替换', '是否中止当前正在执行任务?(任务所得番茄币将重置)',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                self.taskCheckSignal.emit(False)
                return
            else:
                self.task = {}
        self.taskCheckSignal.emit(True)
        self.task = dict
        self.task['tomato_count'] = self.task['task_during'] // 15 if self.task['task_during'] % 15 == 0 else self.task['task_during'] // 15 + 1
        self.taskTitleLabel.setText(self.task['task_name'])
        self.totalTomatoLabel.setText(str(self.task['tomato_count']))
        self.task['tomato_collected'] = 0
        self.task['current_time_left'] = 0
        self.task['task_stage'] = '初始化'
        self.taskStageShow()

    #任务进程信息显示
    def taskStageShow(self):
        if self.task['current_time_left'] == 0:
            self.timer.stop()
            if self.task['task_stage'] == '工作中':
                self.task['tomato_collected'] += 1
                self.task['task_during'] -= 15
                if self.task['tomato_collected'] == self.task['tomato_count']:
                    text = '''任务已全部完成，番茄币已到账'''
                    self.messageView.show(text).showAnimation()
                    self.taskfinish()
                    return
                elif self.task['tomato_collected'] % 4 == 0:
                    text = '''完成一个阶段了，休息25分钟后继续加油'''
                    self.messageView.show(text).showAnimation()
                    self.task['current_time_left'] = 25 * 60
                    self.task['task_stage'] = '长休息'
                else:
                    text = '''已完成1个番茄钟，休息5分钟吧'''
                    self.messageView.show(text).showAnimation()
                    self.task['current_time_left'] = 5 * 60
                    self.task['task_stage'] = '短休息'
            elif self.task['task_stage'] == '短休息' or self.task['task_stage'] == '长休息':
                text = '''休息结束，继续番茄钟吧'''
                self.messageView.show(text).showAnimation()
                if self.task['task_during'] >=15:
                    self.task['current_time_left'] = 15 * 60
                else:
                    self.task['current_time_left'] = self.task['task_during'] * 60
                self.task['task_stage'] = '工作中'
            else:
                if self.task['task_during'] >=15:
                    self.task['current_time_left'] = 15 * 60
                else:
                    self.task['current_time_left'] = self.task['task_during'] * 60
                self.task['task_stage'] = '工作中'
            self.readyTomatoLabel.setText(str(self.task['tomato_collected']))
            self.tomatoStageLabel.setText(self.task['task_stage'])
            self.timeBar.setValue(self.task['current_time_left'])
            self.timeBar.setMaximum(self.task['current_time_left'])
            self.timeLcd.display("%d:%02d" % (self.task['current_time_left']/60,self.task['current_time_left'] % 60))
            self.timer.start(1000)
        else:
            self.task['current_time_left'] -= 1
        self.timeLcd.display("%d:%02d" % (self.task['current_time_left']/60,self.task['current_time_left'] % 60))
        self.timeBar.setValue(self.task['current_time_left'])

    def taskfinish(self):
        self.readyTomatoLabel.setText(str(self.task['tomato_collected']))
        self.tomatoStageLabel.setText("已完成")
        self.timeBar.setValue(0)
        self.timeBar.setMaximum(100)
        self.timeLcd.display("00:00")

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

