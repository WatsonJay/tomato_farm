# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 11:00
# @Author  : Jaywatson
# @File    : PieChartView.py
# @Soft    : tomato_farm
from PyQt5.QtChart import QChartView, QChart, QPieSeries
from PyQt5.QtCore import QMargins
from PyQt5.QtGui import QPainter


class pieChartView(QChartView):

    def __init__(self, *args, **kwargs):
        super(pieChartView, self).__init__(*args, **kwargs)
        self.initChart()

    def initChart(self):
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
        self._series = QPieSeries()
        self.setChart(self._chart)
