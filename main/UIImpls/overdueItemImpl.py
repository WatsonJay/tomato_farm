# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 17:19
# @Author  : Jaywatson
# @File    : overdueItemImpl.py
# @Soft    : tomato_farm
import datetime

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from UI.overdueListItem import Ui_overdueListItem

class overdueItemImpl(QWidget, Ui_overdueListItem):

    # 信号槽
    taskStartSignal = pyqtSignal(dict)
    taskUnlinkSignal = pyqtSignal(str)

    # 初始化
    def __init__(self, parent=None):
        super(overdueItemImpl, self).__init__(parent)
        self.setupUi(self)
        self.doingLabel.setVisible(False)
        self.doingLabel.setText("正在执行")
        self.task = {}
        self.startButton.clicked.connect(self.startTask)
        self.deleteButton.clicked.connect(self.unlink)

    # 信息填充
    def setInfo(self, data):
        self.task = data
        week_day_dict = {
            '0': '星期一',
            '1': '星期二',
            '2': '星期三',
            '3': '星期四',
            '4': '星期五',
            '5': '星期六',
            '6': '星期天',
        }
        week = datetime.datetime.strptime(data['link_date'], "%Y-%m-%d").strftime("%w")
        self.dateLabel.setText(week_day_dict[week]+" "+data['link_date'])
        self.taskNameLabel.setText(data['task_name'],"white")
        if data['is_doing'] == 1:
            self.startButton.setVisible(False)
            self.deleteButton.setVisible(False)
            self.doingLabel.setVisible(True)
        else:
            self.startButton.setVisible(True)
            self.deleteButton.setVisible(True)
            self.doingLabel.setVisible(False)

    # 启动任务
    def startTask(self):
        self.taskStartSignal.emit(self.task)

    # 解绑任务
    def unlink(self):
        self.taskUnlinkSignal.emit(self.task['id'])