# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:31
# @Author  : Jaywatson
# @File    : firstWidgetImpl.py
# @Soft    : tomato_farm
import datetime

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from UI.firstWidget import Ui_homeWidget
from UIImpls.firstItemImpl import firstItemImpl
from UIImpls.messageWidgetImpl import messageWidgetImpl
from UIImpls.tipImpl import tipImpl
from util.loadData import sqlite
from util.logger import logger


class firstWidgetImpl(QWidget, Ui_homeWidget, tipImpl):
    # 信号槽
    taskStartSignal = pyqtSignal()
    taskRefreshSignal = pyqtSignal()
    # 初始化
    def __init__(self, parent=None):
        super(firstWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        log = logger()
        self.messageView = messageWidgetImpl()
        self.conffirst = log.getlogger('gui')
        self.sqlite = sqlite('./config/tomato.db')
        self.loadTodayTask()

    #全部刷新
    def refreshAll(self):
        self.loadTodayTask()
        self.loadOverdueTask()
        print("first")

    #加载今日任务
    def loadTodayTask(self):
        self.todayListWidget.clear()
        now = str(datetime.date.today())
        try:
            sql = '''select tbt.id, tbt.task_name, tbt.task_during, ttld.is_doing from t_base_task tbt
                  join t_task_link_date ttld on tbt.id = ttld.task_id
                  where tbt.is_dated = ? and tbt.is_overdue = ? and tbt.is_finish = ? and ttld.link_date = ?'''
            datas = self.sqlite.executeQuery(sql, 1, 0, 0, now)
            for data in datas:
                taskItem, ListItem = self.makeItem(data)
                self.todayListWidget.addItem(ListItem)
                self.todayListWidget.setItemWidget(ListItem, taskItem)
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conffirst.error(e)

    #加载过期任务
    def loadOverdueTask(self):
        self.overdueListWidget.clear()
        now = str(datetime.date.today())
        try:
            sql = '''select tbt.id, tbt.task_name, tbt.task_during, ttld.is_doing from t_base_task tbt
                  join t_task_link_date ttld on tbt.id = ttld.task_id
                  where tbt.is_dated = ? and tbt.is_overdue = ? and tbt.is_finish = ?'''
            datas = self.sqlite.executeQuery(sql, 1, 1, 0)
            for data in datas:
                taskItem, ListItem = self.makeItem(data)
                self.overdueListWidget.addItem(ListItem)
                self.overdueListWidget.setItemWidget(ListItem, taskItem)
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conffirst.error(e)

    #开始任务
    def startTask(self,id):
        try:
            sql = "Update t_task_link_date set is_doing = 1 where task_id = ?"
            self.sqlite.execute(sql, id)
            self.refreshAll()
            text = '''任务已启动，加油！
请关注你的番茄成长进度'''
            self.messageView.show(text).showAnimation()
            self.taskRefreshSignal.emit()
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conftask.error(e)

    # 解除任务
    def unlinkTask(self, id):
        try:
            sql = "Delete from t_task_link_date where task_id = ?"
            self.sqlite.execute(sql, id)
            sql = "Update t_base_task set is_dated = 0 where id = ?"
            self.sqlite.execute(sql, id)
            self.Tips("已解除任务")
            self.refreshAll()
            self.taskRefreshSignal.emit()
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conftask.error(e)

    # 创建列表项
    def makeItem(self, data):
        firstItem = firstItemImpl()
        firstItem.setInfo(data)
        firstItem.taskStartSignal.connect(self.startTask)
        firstItem.taskUnlinkSignal.connect(self.unlinkTask)
        listItem = QListWidgetItem()
        listItem.setSizeHint(firstItem.size())
        return firstItem, listItem
