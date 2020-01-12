# -*- coding: utf-8 -*-
# @Time    : 2019/12/29 23:22
# @Author  : Jaywatson
# @File    : firstItemImpl.py
# @Soft    : tomato_farm

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from UI.firstWidgetItem import Ui_firstWidgetItem
from UIImpls.tipImpl import tipImpl


class firstItemImpl(QWidget, Ui_firstWidgetItem):
    # 信号槽
    taskStartSignal = pyqtSignal(dict)
    taskUnlinkSignal = pyqtSignal(str)

    # 初始化
    def __init__(self, parent=None):
        super(firstItemImpl, self).__init__(parent)
        self.setupUi(self)
        self.dict = {}
        self.doingLabel.setVisible(False)
        self.doingLabel.setText("正在执行")
        self.startButton.clicked.connect(self.startTask)
        self.deleteButton.clicked.connect(self.unlink)

    #信息填充
    def setInfo(self,data):
        self.taskNameLabel.setText(data['task_name'])
        self.duringLabel.setText(str(data['task_during']))
        self.dict = data
        if data['is_doing'] == 1:
            self.startButton.setVisible(False)
            self.deleteButton.setVisible(False)
            self.doingLabel.setVisible(True)
        else:
            self.startButton.setVisible(True)
            self.deleteButton.setVisible(True)
            self.doingLabel.setVisible(False)

    #启动任务
    def startTask(self):
        self.taskStartSignal.emit(self.dict)

    #解绑任务
    def unlink(self):
        self.taskUnlinkSignal.emit(self.dict['id'])