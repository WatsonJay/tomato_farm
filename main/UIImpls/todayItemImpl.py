# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 17:20
# @Author  : Jaywatson
# @File    : todayItemImpl.py
# @Soft    : tomato_farm

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from UI.todayListItem import Ui_todayListItem
import UI.icons_rc
from util.loadData import sqlite
from util.logger import logger


class todayItemImpl(QWidget, Ui_todayListItem):
    # 信号槽
    taskStartSignal = pyqtSignal(dict)
    taskUnlinkSignal = pyqtSignal(str)
    taskTopSignal = pyqtSignal(str,str)

    # 初始化
    def __init__(self, parent=None):
        super(todayItemImpl, self).__init__(parent)
        self.setupUi(self)
        self.task = {}
        self.top = 0
        log = logger()
        self.doingLabel.setVisible(False)
        self.doingLabel.setText("正在执行")
        self.conftodo = log.getlogger('gui')
        self.upIcon = QtGui.QIcon()
        self.upIcon.addPixmap(QtGui.QPixmap(":/icon/top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downIcon = QtGui.QIcon()
        self.downIcon.addPixmap(QtGui.QPixmap(":/icon/untop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.topButton.clicked.connect(self.topTask)
        self.startButton.clicked.connect(self.startTask)
        self.deleteButton.clicked.connect(self.unlink)

    # 信息填充
    def setInfo(self, data):
        if data['is_top'] == 1:
            self.top = 1
            self.radiusLabel.setStyleSheet("#radiusLabel{border-radius:6px;background:#FEE66E;}")
            self.topButton.setIcon(self.downIcon)
        else:
            self.top = 0
            self.topButton.setIcon(self.upIcon)
        self.task = data
        self.taskNameLabel.setText(data['task_name'], "white")
        if data['is_doing'] == 1:
            self.topButton.setVisible(False)
            self.startButton.setVisible(False)
            self.deleteButton.setVisible(False)
            self.doingLabel.setVisible(True)
        else:
            self.topButton.setVisible(True)
            self.startButton.setVisible(True)
            self.deleteButton.setVisible(True)
            self.doingLabel.setVisible(False)

    # 任务置顶
    def topTask(self):
        if self.top == 1:
            sql = "Update t_task_link_date set is_top = 0 where task_id = ?"
            self.top = 0
            self.topButton.setIcon(self.upIcon)
            self.radiusLabel.setStyleSheet("#radiusLabel{border-radius:6px;background:white;}")
        else:
            sql = "Update t_task_link_date set is_top = 1 where task_id = ?"
            self.top = 1
            self.topButton.setIcon(self.downIcon)
            self.radiusLabel.setStyleSheet("#radiusLabel{border-radius:6px;background:#FEE66E;}")
        self.taskTopSignal.emit(self.task['id'], sql)

    # 启动任务
    def startTask(self):
        self.taskStartSignal.emit(self.task)

    # 解绑任务
    def unlink(self):
        self.taskUnlinkSignal.emit(self.task['id'])