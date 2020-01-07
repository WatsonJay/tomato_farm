# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 9:44
# @Author  : Jaywatson
# @File    : miniBarImpl.py
# @Soft    : tomato_farm

from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import QWidget, QMessageBox
from UI.miniBar import Ui_miniBarForm
from UIImpls.messageWidgetImpl import messageWidgetImpl
from UIImpls.noBorderImpl import noBorderImpl
from UIImpls.tipImpl import tipImpl
from util.loadConf import config
from util.logger import logger


class miniBarImpl(QWidget, Ui_miniBarForm, noBorderImpl, tipImpl):
    # 信号槽
    normalSizeSignal = pyqtSignal(dict)
    taskFinishSignal = pyqtSignal()
    taskStopSignal = pyqtSignal()

    # 初始化
    def __init__(self, parent=None):
        super(miniBarImpl, self).__init__(parent)
        self.setupUi(self)
        self.conf = config()
        log = logger()
        self.confmini = log.getlogger('gui')
        self.task = {}
        self.timer = QTimer()
        self.messageView = messageWidgetImpl()
        self.move(int(self.conf.getOption('miniBar', 'placeX')), int(self.conf.getOption('miniBar', 'placeY')))
        self.taskLabel.setText("无","white")
        self.normalSizeButton.clicked.connect(self.normalSize)
        self.timer.timeout.connect(self.taskStageShow)
        self.redoButton.clicked.connect(self.redoTask)
        self.startButton.clicked.connect(self.startTask)
        self.pauseButton.clicked.connect(self.pauseTask)
        self.stopButton.clicked.connect(self.stopTask)


    #切换正常界面
    def normalSize(self):
        self.normalSizeSignal.emit(self.task)
        self.taskLabel.setText("","white")
        self.tomatoStageLabel.setText("")
        self.timeBar.setValue(0)
        self.timeBar.setMaximum(100)
        self.timeLcd.display("00:00")
        self.task = {}
        self.timer.stop()
        self.conf.addoption('miniBar', 'placeX', str(self.x()))
        self.conf.addoption('miniBar', 'placeY', str(self.y()))

    # 切换迷你界面
    def miniShow(self,dist):
        self.task = dist
        if self.task != {}:
            self.taskLabel.setText(self.task['task_name'],"white")
            self.tomatoStageLabel.setText(self.task['task_stage'])
            self.timeBar.setMaximum(self.task['stage_time'])
            self.timeBar.setValue(self.task['current_time_left'])
            self.timeLcd.display("%d:%02d" % (self.task['current_time_left']/60,self.task['current_time_left'] % 60))
            if self.task['pause'] == 0:
                self.timer.start(1000)
        self.show()

    # 任务进程信息显示
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
                    self.task['current_time_left'] = self.task['stage_time'] = 25 * 60
                    self.task['task_stage'] = '长休息'
                else:
                    text = '''已完成1个番茄钟，休息5分钟吧'''
                    self.messageView.show(text).showAnimation()
                    self.task['current_time_left'] = self.task['stage_time'] = 5 * 60
                    self.task['task_stage'] = '短休息'
            else:
                if self.task['task_stage'] == '短休息' or self.task['task_stage'] == '长休息':
                    text = '''休息结束，继续番茄钟吧'''
                    self.messageView.show(text).showAnimation()
                if self.task['task_during'] >= 15:
                    self.task['current_time_left'] = self.task['stage_time'] = 15 * 60
                else:
                    self.task['current_time_left'] = self.task['stage_time'] = self.task['task_during'] * 60
                self.task['task_stage'] = '工作中'
            self.timeBar.setValue(self.task['current_time_left'])
            self.timeBar.setMaximum(self.task['stage_time'])
            self.timeLcd.display("%d:%02d" % (self.task['stage_time'] / 60, self.task['stage_time'] % 60))
            self.timer.start(1000)
        else:
            self.task['current_time_left'] -= 1
        self.timeLcd.display("%d:%02d" % (self.task['current_time_left'] / 60, self.task['current_time_left'] % 60))
        self.timeBar.setValue(self.task['current_time_left'])

    # 重启任务
    def redoTask(self):
        if self.task != {}:
            reply = QMessageBox.question(self, '重置任务', '是否重置当前正在执行任务?(任务所得番茄币将重置)',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.timer.stop()
                self.task['tomato_collected'] = 0
                self.task['current_time_left'] = 0
                self.task['task_stage'] = '初始化'
                self.taskStageShow()
            else:
                return

    # 开始任务
    def startTask(self):
        if self.task['pause'] == 1 and self.task != {}:
            self.timer.start(1000)
            self.task['pause'] = 0

    # 暂停任务
    def pauseTask(self):
        if self.task != {}:
            self.timer.stop()
            self.task['pause'] = 1

    # 停止任务
    def stopTask(self):
        if self.task != {}:
            self.taskStopSignal.emit()
            self.task = {}
            self.normalSize()

    #任务完成
    def taskfinish(self):
        self.taskFinishSignal.emit()
        self.task = {}
        self.normalSize()
