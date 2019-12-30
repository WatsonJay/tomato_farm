# -*- coding: utf-8 -*-
# @Time    : 2019/12/29 23:22
# @Author  : Jaywatson
# @File    : firstItemImpl.py
# @Soft    : tomato_farm

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from UI.firstWidgetItem import Ui_firstWidgetItem
from UIImpls.tipImpl import tipImpl


class firstItemImpl(QWidget, Ui_firstWidgetItem, tipImpl):
    # 信号槽
    taskStartSignal = pyqtSignal(str)
    taskUnlinkSignal = pyqtSignal(str)

    # 初始化
    def __init__(self, parent=None):
        super(firstItemImpl, self).__init__(parent)
        self.setupUi(self)
        self.taskId = ''
        self.during = 0
        self.startButton.clicked.connect(self.startTask)
        self.deleteButton.clicked.connect(self.unlink)

    #信息填充
    def setInfo(self,data):
        self.taskId = data['id']
        self.taskNameLabel.setText(data['task_name'])
        self.during = data['task_during']
        self.duringLabel.setText(str(data['task_during']))

    #启动任务
    def startTask(self):
        self.taskStartSignal.emit(self.taskId)

    #解绑任务
    def unlink(self):
        self.taskUnlinkSignal.emit(self.taskId)