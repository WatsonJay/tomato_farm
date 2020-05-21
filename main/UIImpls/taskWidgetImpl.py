# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:36
# @Author  : Jaywatson
# @File    : taskWidgetImpl.py
# @Soft    : tomato_farm
import datetime
import uuid

from PyQt5.QtCore import QDate, pyqtSignal
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QMessageBox

from UI.taskWidget import Ui_taskWidget
from UIImpls.taskItemImpl import taskItemImpl
from UIImpls.tipImpl import tipImpl
from util.loadData import sqlite
from util.logger import logger


class taskWidgetImpl(QWidget, Ui_taskWidget, tipImpl):
    #信号槽
    taskRefreshSignal = pyqtSignal()
    # 初始化
    def __init__(self, parent=None):
        super(taskWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        self.setMouseTracking(True)
        log = logger()
        self.conftask = log.getlogger('gui')
        self.sqlite = sqlite('/config/tomato.db')
        self.id=''
        self.taskDeadLineEdit.setMinimumDate(QDate.currentDate())
        #功能绑定
        self.addTaskButton.clicked.connect(self.addTask)
        self.modifTaskButton.clicked.connect(self.modifTask)
        self.delTaskButton.clicked.connect(self.deletTask)
        self.cancleButton.clicked.connect(self.cancel)
        self.commitButton.clicked.connect(self.commitTask)
        self.calendarWidget.clicked.connect(self.currentDayTask)
        self.linkDayButton.clicked.connect(self.taskLinkDay)
        self.undoLinkButton.clicked.connect(self.taskUnlinkDay)

    #全部刷新
    def refreshAll(self):
        self.loadTask()
        self.loadHistoryTask()
        self.currentDayTask()

    # 列出所有任务
    def loadTask(self):
            self.taskListWidget.clear()
            try:
                sql = "select * from t_base_task where is_dated = ? and is_finish = ?"
                datas = self.sqlite.executeQuery(sql, 0, 0)
                for data in datas:
                    taskItem, ListItem = self.makeItem(data)
                    self.taskListWidget.addItem(ListItem)
                    self.taskListWidget.setItemWidget(ListItem, taskItem)
            except Exception as e:
                self.Tips("系统异常，请查看日志")
                self.conftask.error(e)

    # 列出历史任务
    def loadHistoryTask(self):
            self.historyListWidget.clear()
            try:
                sql = "select * from t_base_task where is_finish = ?"
                datas = self.sqlite.executeQuery(sql, 1)
                for data in datas:
                    taskItem, ListItem = self.makeItem(data)
                    self.historyListWidget.addItem(ListItem)
                    self.historyListWidget.setItemWidget(ListItem, taskItem)
            except Exception as e:
                self.Tips("系统异常，请查看日志")
                self.conftask.error(e)

    # 列出当日任务
    def currentDayTask(self):
            date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
            self.dayTaskListWidget.clear()
            try:
                sql = '''
                select 
                    tbt.id,tbt.task_name,tbt.deadline_time,tbt.task_during,tbt.is_overdue,tbt.is_dated,tbt.is_finish,tbt.task_desc
                from 
                    t_task_link_date ttld 
                join 
                    t_base_task tbt on ttld.task_id=tbt.id
                where
                    tbt.is_finish = 0 
                and
                    ttld.link_date = ?
                '''
                datas = self.sqlite.executeQuery(sql, date)
                for data in datas:
                    taskItem, ListItem = self.makeItem(data)
                    self.dayTaskListWidget.addItem(ListItem)
                    self.dayTaskListWidget.setItemWidget(ListItem, taskItem)
            except Exception as e:
                self.Tips("系统异常，请查看日志")
                self.conftask.error(e)

    #新增任务
    def addTask(self):
        self.id = ''
        self.taskNameEdit.setText("")
        self.taskHourBox.setValue(0)
        self.taskMinuteBox.setValue(1)
        self.taskDeadLineEdit.setDate(QDate.currentDate())
        self.taskDescEdit.setText("")
        self.stackedWidget.setCurrentIndex(1)

    #编辑任务
    def modifTask(self):
        if len(self.taskListWidget.selectedItems()) > 0:
            selectedItem = self.taskListWidget.itemWidget(self.taskListWidget.selectedItems()[0])
            self.id = selectedItem.taskId
            self.taskNameEdit.setText(selectedItem.taskNameLabel.text())
            self.taskHourBox.setValue(selectedItem.during//60)
            self.taskMinuteBox.setValue(selectedItem.during%60)
            self.taskDeadLineEdit.setDate(QDate.fromString(selectedItem.date,'yyyy-MM-dd'))
            self.taskDescEdit.setText(selectedItem.desc)
            self.stackedWidget.setCurrentIndex(1)

    # 删除任务
    def deletTask(self):
        try:
            if len(self.taskListWidget.selectedItems()) > 0:
                reply = QMessageBox.question(self, '删除确认', '你确定要删除吗?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    selectedItem = self.taskListWidget.itemWidget(self.taskListWidget.selectedItems()[0])
                    id = selectedItem.taskId
                    sql = "Delete from t_base_task where id = ?"
                    self.sqlite.execute(sql,id)
                    self.Tips("已删除任务")
                    self.loadTask()
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conftask.error(e)

    #提交任务
    def commitTask(self):
        try:
            if self.taskNameEdit.text()!='':
                if self.id == '':
                    sql = "Insert Into t_base_task (id,task_name,deadline_time,task_during,task_desc) values (?,?,?,?,?)"
                    time = self.taskHourBox.value() * 60 + self.taskMinuteBox.value()
                    self.sqlite.execute(sql,[str(uuid.uuid1()), self.taskNameEdit.text(), self.taskDeadLineEdit.text(), time,self.taskDescEdit.toPlainText()])
                else:
                    sql = "Update t_base_task SET task_name=?,deadline_time=?,task_during=?,task_desc=?,is_overdue=0 where id=?"
                    time = self.taskHourBox.value() * 60 + self.taskMinuteBox.value()
                    self.sqlite.execute(sql,[self.taskNameEdit.text(),self.taskDeadLineEdit.text(),time,self.taskDescEdit.toPlainText(),self.id])
                self.Tips("提交成功")
                self.stackedWidget.setCurrentIndex(0)
                self.loadTask()
                self.id = ''
            else:
                self.Tips("请填写任务名")
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conftask.error(e)
            self.id = ''

    #取消
    def cancel(self):
        self.stackedWidget.setCurrentIndex(0)
        self.id = ''

    # 任务分配
    def taskLinkDay(self):
        try:
            if len(self.taskListWidget.selectedItems()) > 0:
                date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
                now = datetime.date.today()
                if datetime.datetime.strptime(date, "%Y-%m-%d").date() >= now:
                    selectedItem = self.taskListWidget.itemWidget(self.taskListWidget.selectedItems()[0])
                    if datetime.datetime.strptime(selectedItem.date, "%Y-%m-%d").date() >= datetime.datetime.strptime(date, "%Y-%m-%d").date():
                        id = selectedItem.taskId
                        sql = "Insert Into t_task_link_date (id,task_id,link_date) values (?,?,?)"
                        self.sqlite.execute(sql,[str(uuid.uuid1()), id, date])
                        sql = "Update t_base_task set is_dated = 1 where id = ?"
                        self.sqlite.execute(sql,id)
                        self.Tips("绑定成功")
                        self.loadTask()
                        self.currentDayTask()
                        self.taskRefreshSignal.emit()
                    else:
                        self.Tips("任务截至时间低于分配时间")
                else:
                    self.Tips("不可将任务分配给过去时间")
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conftask.error(e)

    # 任务取消分配
    def taskUnlinkDay(self):
        try:
            if len(self.dayTaskListWidget.selectedItems()) > 0:
                selectedItem = self.dayTaskListWidget.itemWidget(self.dayTaskListWidget.selectedItems()[0])
                id = selectedItem.taskId
                sql = "Delete from t_task_link_date where task_id = ?"
                self.sqlite.execute(sql,id)
                sql = "Update t_base_task set is_dated = 0,is_overdue = 0 where id = ?"
                self.sqlite.execute(sql, id)
                self.Tips("已解除任务")
                self.loadTask()
                self.currentDayTask()
                self.taskRefreshSignal.emit()
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conftask.error(e)

    # 创建列表项
    def makeItem(self,data):
        taskItem = taskItemImpl()
        taskItem.setInfo(data)
        ListItem = QListWidgetItem()
        ListItem.setSizeHint(taskItem.size())
        return taskItem,ListItem