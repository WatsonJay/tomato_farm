# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:36
# @Author  : Jaywatson
# @File    : taskWidgetImpl.py
# @Soft    : tomato_farm
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from UI.taskWidget import Ui_taskWidget
from UIImpls.taskItemImpl import taskItemImpl
from util.loadData import sqlite


class taskWidgetImpl(QWidget, Ui_taskWidget):
    # 初始化
    def __init__(self, parent=None):
        super(taskWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        self.sqlite = sqlite('./config/tomato.db')
        self.addTaskButton.clicked.connect(self.addTask)
        self.cancleButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))


    def addTask(self):
        self.taskNameEdit.setText("")
        self.taskHourBox.setValue(0)
        self.taskMinuteBox.setValue(1)
        self.taskDeadLineEdit.setDate(QDate.currentDate())
        self.taskDescEdit.setText("")
        self.stackedWidget.setCurrentIndex(1)

    def loadTask(self):
        sql = "select * from "
        taskItem = taskItemImpl()
        ListItem = QListWidgetItem()
        ListItem.setSizeHint(taskItem.size())
        self.taskListWidget.addItem(ListItem)
        self.taskListWidget.setItemWidget(ListItem, taskItem)