# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 11:45
# @Author  : Jaywatson
# @File    : perBarChartView.py
# @Soft    : tomato_farm
from PyQt5.QtChart import QChartView, QChart, QBarCategoryAxis, QValueAxis, QPercentBarSeries, QBarSet
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtGui import QPainter


class perBarChartView(QChartView):

    def __init__(self, xAxis=[], *args, **kwargs):
        super(perBarChartView, self).__init__(*args, **kwargs)
        self.initChart(xAxis)

    def initChart(self, xAxis):
        self._chart = QChart()
        #调整边距
        self._chart.layout().setContentsMargins(0, 0, 0, 0) #外界
        self._chart.setMargins(QMargins(3, 0, 3, 0)) #内界
        self._chart.setBackgroundRoundness(0)
        self._chart.setBackgroundVisible(False)
        #设置主题
        self._chart.setTheme(QChart.ChartThemeBlueIcy)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)
        # 开启动画效果
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        self.categories = xAxis
        self._series = QPercentBarSeries(self._chart)
        self._chart.addSeries(self._series)
        axis_x = QBarCategoryAxis(self._chart)
        axis_x.append(self.categories)
        axis_x.setLabelsAngle(280)
        axis_y = QValueAxis(self._chart)
        axis_y.setTitleText("比例")
        axis_y.setRange(0, 100)
        self._chart.addAxis(axis_x, Qt.AlignBottom)
        self._chart.addAxis(axis_y, Qt.AlignLeft)
        self._series.attachAxis(axis_x)
        self._series.attachAxis(axis_y)
        self.setChart(self._chart)