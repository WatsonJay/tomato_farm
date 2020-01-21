# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 21:36
# @Author  : Jaywatson
# @File    : monthChartView.py
# @Soft    : tomato_farm

from PyQt5.QtChart import QChartView, QChart, QBarCategoryAxis, QBarSeries, QValueAxis, QPercentBarSeries
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtGui import QPainter


class monthChartView(QChartView):

    def __init__(self, xAxis=[], *args, **kwargs):
        super(monthChartView, self).__init__(*args, **kwargs)
        self.initChart(xAxis)

    def initChart(self, xAxis):
        self._chart = QChart()
        # 调整边距
        self._chart.layout().setContentsMargins(0, 0, 0, 0)  # 外界
        self._chart.setMargins(QMargins(3, 0, 3, 0))  # 内界
        self._chart.setBackgroundRoundness(0)
        self._chart.setBackgroundVisible(False)
        # 设置主题
        self._chart.setTheme(QChart.ChartThemeBlueIcy)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)
        # 开启动画效果
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        self.categories = xAxis
        self._series = QBarSeries(self._chart)
        self._chart.addSeries(self._series)
        self._chart.createDefaultAxes()  # 创建默认的轴
        self._axis_x = QBarCategoryAxis(self._chart)
        self._axis_x.append(self.categories)
        self._axis_y = QValueAxis(self._chart)
        self._axis_y.setTitleText("任务数")
        self._axis_y.setRange(0, 10)
        self._chart.setAxisX(self._axis_x, self._series)
        self._chart.setAxisY(self._axis_y, self._series)
        self.setChart(self._chart)