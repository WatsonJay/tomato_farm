# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:36
# @Author  : Jaywatson
# @File    : taskWidgetImpl.py
# @Soft    : tomato_farm
import uuid

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from UI.taskWidget import Ui_taskWidget
from UIImpls.taskItemImpl import taskItemImpl
from UIImpls.tipImpl import tipImpl
from util.loadData import sqlite
from util.logger import logger


class taskWidgetImpl(QWidget, Ui_taskWidget, tipImpl):
    # 初始化
    def __init__(self, parent=None):
        super(taskWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        log = logger()
        self.conftask = log.getlogger('gui')
        self.sqlite = sqlite('./config/tomato.db')
        self.loadTask()
        self.addTaskButton.clicked.connect(self.addTask)
        self.cancleButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.commitButton.clicked.connect(self.commitTask)

    def addTask(self):
        self.taskNameEdit.setText("")
        self.taskHourBox.setValue(0)
        self.taskMinuteBox.setValue(1)
        self.taskDeadLineEdit.setDate(QDate.currentDate())
        self.taskDescEdit.setText("")
        self.stackedWidget.setCurrentIndex(1)

    def commitTask(self):
        try:
            sql = "Insert Into t_base_task (id,task_name,deadline_time,task_during,task_desc) values (?,?,?,?,?)"
            time = self.taskHourBox.value() * 60 + self.taskMinuteBox.value()
            self.sqlite.execute(sql,[str(uuid.uuid1()),self.taskNameEdit.text(),self.taskDeadLineEdit.text(),time,self.taskDescEdit.toPlainText()])
            self.Tips("新增成功")
            self.stackedWidget.setCurrentIndex(0)
            self.loadTask()
        except Exception as e:
            self.conftask.error(e)


    def loadTask(self):
        sql = "select * from t_base_task where is_dated = ? and is_overdue = ? and is_finish = ?"
        datas = self.sqlite.executeQuery(sql,0,0,0)
        for data in datas:
            taskItem = taskItemImpl()
            taskItem.setInfo(data)
            ListItem = QListWidgetItem()
            ListItem.setSizeHint(taskItem.size())
            self.taskListWidget.addItem(ListItem)
            self.taskListWidget.setItemWidget(ListItem, taskItem)

