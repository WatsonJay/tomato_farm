# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:34
# @Author  : Jaywatson
# @File    : statisWidgetImpl.py
# @Soft    : tomato_farm
from random import randint

import PyQt5
from PyQt5.QtChart import QBarSet
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

import UI.icons_rc
from UI.statisWidget import Ui_statisWidget
from UIImpls.tipImpl import tipImpl
from util.loadData import sqlite
from util.logger import logger


class statisWidgetImpl(QWidget, Ui_statisWidget, tipImpl):
    # 初始化
    def __init__(self, parent=None):
        super(statisWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        log = logger()
        self.confstatis = log.getlogger('gui')
        self.sqlite = sqlite('./config/tomato.db')

    #触发全部刷新
    def refreshAll(self):
        self.loadCount()
        self.loadYearTotalChart()

    # 加载统计数据
    def loadCount(self):
        try:
            sql = "select * from v_statis_task"
            data = self.sqlite.executeQuery(sql)
            self.todayLabel.setText(str(data[0]['day_count']))
            self.weekLabel.setText(str(data[0]['week_count']))
            self.monthLabel.setText(str(data[0]['month_count']))
            self.totalLabel.setText(str(data[0]['total']))
            self.lastDayLabel.setText(str(data[0]['last_day_count']))
            self.lastWeekLabel.setText(str(data[0]['last_week_count']))
            self.lastMonthLabel.setText(str(data[0]['last_month_count']))
            #比较数据
            if data[0]['day_count'] > data[0]['last_day_count']:
                jpg = QPixmap(":/icon/upLevel.png").scaled(self.dayLevelLabel.width(), self.dayLevelLabel.height())
            elif data[0]['day_count'] < data[0]['last_day_count']:
                jpg = QPixmap(":/icon/downLevel.png").scaled(self.dayLevelLabel.width(), self.dayLevelLabel.height())
            else:
                jpg = QPixmap(":/icon/level.png").scaled(self.dayLevelLabel.width(), self.dayLevelLabel.height())
            self.dayLevelLabel.setPixmap(jpg)
            if data[0]['week_count'] > data[0]['last_week_count']:
                jpg = QPixmap(":/icon/upLevel.png").scaled(self.weekLevelLabel.width(), self.weekLevelLabel.height())
            elif data[0]['week_count'] < data[0]['last_week_count']:
                jpg = QPixmap(":/icon/downLevel.png").scaled(self.weekLevelLabel.width(), self.weekLevelLabel.height())
            else:
                jpg = QPixmap(":/icon/level.png").scaled(self.weekLevelLabel.width(), self.weekLevelLabel.height())
            self.weekLevelLabel.setPixmap(jpg)
            if data[0]['month_count'] > data[0]['last_month_count']:
                jpg = QPixmap(":/icon/upLevel.png").scaled(self.monthLevelLabel.width(), self.monthLevelLabel.height())
            elif data[0]['month_count'] < data[0]['last_month_count']:
                jpg = QPixmap(":/icon/downLevel.png").scaled(self.monthLevelLabel.width(), self.monthLevelLabel.height())
            else:
                jpg = QPixmap(":/icon/level.png").scaled(self.monthLevelLabel.width(), self.monthLevelLabel.height())
            self.monthLevelLabel.setPixmap(jpg)
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confstatis.error(e)

    #年度统计数据
    def loadYearTotalChart(self):
        try:
            sql = 'select * from v_year_total_count'
            datas = self.sqlite.executeQuery(sql)
            yearXAxis = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
            month_day_dict = {
                '01': '一月',
                '02': '二月',
                '03': '三月',
                '04': '四月',
                '05': '五月',
                '06': '六月',
                '07': '七月',
                '08': '八月',
                '09': '九月',
                '10': '十月',
                '11': '十一月',
                '12': '十二月',
            }
            doneBar = QBarSet('按时完成')
            overdueBar = QBarSet('逾期完成')
            # 待优化循环
            for month in yearXAxis:
                exist = False
                for data in datas:
                    if month == month_day_dict[data['month']]:
                        doneBar.append(data['done'])
                        overdueBar.append(data['overdue'])
                        exist =True
                        continue
                if exist == False :
                    doneBar.append(0)
                    overdueBar.append(0)
            self.yearTotalView._series.append(doneBar)
            self.yearTotalView._series.append(overdueBar)

        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confstatis.error(e)




