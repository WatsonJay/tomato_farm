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
    taskStartSignal = pyqtSignal(dict)
    taskRefreshSignal = pyqtSignal()

    # 初始化
    def __init__(self, parent=None):
        super(firstWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        log = logger()
        self.taskRan = False
        self.messageView = messageWidgetImpl()
        self.conffirst = log.getlogger('gui')
        self.sqlite = sqlite('/config/tomato.db')

    # 任务刷新
    def refreshAll(self):
        self.loadTodayTask()
        self.loadOverdueTask()
        self.loadTaskCount()
        self.refreshAllCoin()

    # 番茄币刷新
    def refreshAllCoin(self):
        self.loadCoin()
        self.sumCoin()

    # 加载今日任务
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

    # 加载过期任务
    def loadOverdueTask(self):
        self.overdueListWidget.clear()
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

    # 加载金币记录
    def loadTaskCount(self):
        try:
            sql = "select * from v_task_count"
            datas = self.sqlite.executeQuery(sql)
            self.totalTaskLabel.setText(str(datas[0]['total']))
            self.overdueTaskLabel.setText(str(datas[0]['overdue']))
            self.completeTaskLabel.setText(str(datas[0]['done']))
            self.undoTaskLabel.setText(str(datas[0]['left']))
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conffirst.error(e)

    # 加载金币记录
    def loadCoin(self):
        self.billTextBrowser.clear()
        try:
            sql = "select * from t_base_coin"
            datas = self.sqlite.executeQuery(sql)
            for data in datas:
                if data['coin_type'] == 0:
                    type = '进账'
                else:
                    type = '支出'
                msg = data['create_time']+"   "+data['desc']+type+"番茄币"+str(data['coin_number'])+"个"
                self.billTextBrowser.append(msg)
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conffirst.error(e)

    # 统计番茄币
    def sumCoin(self):
        try:
            sql = "select (select ifNull(sum(coin_number),0) as 'in' from t_base_coin Where coin_type = 0) - (select ifNull(sum(coin_number),0) as 'in' from t_base_coin Where coin_type = 1) as sum"
            datas = self.sqlite.executeQuery(sql)
            coinSum = datas[0]['sum']
            self.tomatoCoinLabel.setText(str(coinSum))
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conffirst.error(e)

    # 检查
    def taskCheck(self, bool):
        self.taskRan = bool

    # 开始任务
    def startTask(self,dict):
        try:
            self.taskStartSignal.emit(dict)
            if self.taskRan:
                text = '''任务已启动，加油！
请关注你的番茄成长进度'''
                self.messageView.show(text).showAnimation()
                sql = "Update t_task_link_date set is_doing = 1 where task_id = ?"
                self.sqlite.execute(sql, dict['id'])
                self.refreshAll()
                self.taskRefreshSignal.emit()
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conffirst.error(e)

    # 解除任务
    def unlinkTask(self, id):
        try:
            sql = "Delete from t_task_link_date where task_id = ?"
            self.sqlite.execute(sql, id)
            sql = "Update t_base_task set is_dated = 0,is_overdue = 0 where id = ?"
            self.sqlite.execute(sql, id)
            self.Tips("已解除任务")
            self.refreshAll()
            self.taskRefreshSignal.emit()
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.conffirst.error(e)

    # 创建列表项
    def makeItem(self, data):
        firstItem = firstItemImpl()
        firstItem.setInfo(data)
        firstItem.taskStartSignal.connect(self.startTask)
        firstItem.taskUnlinkSignal.connect(self.unlinkTask)
        listItem = QListWidgetItem()
        listItem.setSizeHint(firstItem.size())
        return firstItem, listItem
