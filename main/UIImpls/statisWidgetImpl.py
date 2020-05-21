# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:34
# @Author  : Jaywatson
# @File    : statisWidgetImpl.py
# @Soft    : tomato_farm
from datetime import datetime

from PyQt5.QtChart import QBarSet
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QWidget
import calendar
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
        self.setMouseTracking(True)
        log = logger()
        self.confstatis = log.getlogger('gui')
        self.sqlite = sqlite('/config/tomato.db')
        self.searchButton.clicked.connect(self.search)
        self.weekRefreshButton.clicked.connect(self.reloadWeek)
        self.monthRefreshButton.clicked.connect(lambda :self.loadMonthChart('', ''))

    #触发全部刷新
    def refreshAll(self):
        self.loadCount()
        self.loaddate()
        self.loadYearTotalChart()
        self.loadWeekChart()
        self.loadWeekPie()
        self.loadMonthChart()

    def reloadWeek(self):
        self.weekChartView.cal()
        self.weekPieView.refresh()
        self.loadWeekChart()
        self.loadWeekPie()

    def search(self):
        year = self.yearComboBox.currentText()
        month = self.monthComboBox.currentText()
        self.loadMonthChart(year, month)

    #加载月份和年份
    def loaddate(self):
        self.monthComboBox.clear()
        self.yearComboBox.clear()
        sql = "SELECT strftime('%m',tbt.finish_date) as month FROM t_base_task tbt WHERE tbt.finish_date not null  group by month order by month"
        datas = self.sqlite.executeQuery(sql)
        for data in datas:
            self.monthComboBox.addItem(data['month'])
        sql = "SELECT strftime('%Y',tbt.finish_date) as year FROM t_base_task tbt WHERE tbt.finish_date not null group by year order by year"
        datas = self.sqlite.executeQuery(sql)
        for data in datas:
            self.yearComboBox.addItem(data['year'])

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
            self.yearTotalView._series.clear()
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
            doneBar.setColor(QColor('#F95D5C'))
            overdueBar = QBarSet('逾期完成')
            overdueBar.setColor(QColor('#aa3e3e'))
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

    #读取周图表
    def loadWeekChart(self):
        try:
            self.weekChartView._series.clear()
            sql = 'select * from v_week_task_chart'
            datas = self.sqlite.executeQuery(sql)
            weekXAxis = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
            week_day_dict = {
                '0': '星期一',
                '1': '星期二',
                '2': '星期三',
                '3': '星期四',
                '4': '星期五',
                '5': '星期六',
                '6': '星期天',
            }
            doneBar = QBarSet('完成任务')
            doneBar.setColor(QColor('#F95D5C'))
            # 待优化循环
            for week in weekXAxis:
                exist = False
                for data in datas:
                    if week == week_day_dict[data['week']]:
                        doneBar.append(data['count'])
                        if data['count'] > self.weekChartView._axis_y.max():
                            self.weekChartView._axis_y.setRange(0, data['count']+3)
                        exist = True
                        continue
                if exist == False:
                    doneBar.append(0)
                self.weekChartView._series.append(doneBar)
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confstatis.error(e)

    # 读取周圆表
    def loadWeekPie(self):
        try:
            self.weekPieView._series.clear()
            sql = 'select * from v_weeek_task_pie'
            datas = self.sqlite.executeQuery(sql)
            if len(datas) > 0:
                done = self.weekPieView._series.append('按时完成', datas[0]['done'])
                overdue = self.weekPieView._series.append('逾期完成', datas[0]['overdue'])
                undone = self.weekPieView._series.append('未完成', datas[0]['undone'])
            else:
                done = self.weekPieView._series.append('按时完成', 0)
                overdue =self.weekPieView._series.append('逾期完成', 0)
                undone = self.weekPieView._series.append('未完成', 0)
            done.setColor(QColor('#F95D5C'))
            overdue.setColor(QColor('#aa3e3e'))
            undone.setColor(QColor('#faafaf'))
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confstatis.error(e)

    # 读取月图表
    def loadMonthChart(self, year = '', month = ''):
        try:
            self.monthChartView._series.clear()
            self.monthChartView._axis_x.clear()
            if year == '':
                year = datetime.now().strftime('%Y')
            if month == '':
                month = datetime.now().strftime('%m')
            monthRange = calendar.monthrange(int(year), int(month))
            dates = []
            cats = []
            for i in range(monthRange[1]):
                dates.append(str(i+1))
                cats.append(str(i+1) + '日')
            self.monthChartView._axis_x.append(dates)
            self.monthChartView._axis_x.setTitleText('日期')
            self.monthChartView.setCat(cats)
            self.monthChartView.cal()
            sql = '''
            SELECT 
                count( * ) as count,
            CAST(strftime('%d',tbt.finish_date)as int) as day
            FROM t_base_task tbt
            WHERE tbt.is_finish = 1 AND 
                strftime('%m',tbt.finish_date) = ? AND 
                strftime('%Y',tbt.finish_date) = ?
            group by strftime('%m',tbt.finish_date)
            '''
            datas = self.sqlite.executeQuery(sql, [month, year])
            doneBar = QBarSet('完成任务')
            doneBar.setColor(QColor('#F95D5C'))
            # 待优化循环
            for date in dates:
                exist = False
                for data in datas:
                    if date == str(data['day']):
                        doneBar.append(data['count'])
                        if data['count'] > self.weekChartView._axis_y.max():
                            self.monthChartView._axis_y.setRange(0, data['count'] + 3)
                        exist = True
                        continue
                if exist == False:
                    doneBar.append(0)
                self.monthChartView._series.append(doneBar)
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confstatis.error(e)




