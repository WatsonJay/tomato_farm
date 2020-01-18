# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 11:00
# @Author  : Jaywatson
# @File    : BarChartView.py
# @Soft    : tomato_farm
from PyQt5 import Qt
from PyQt5.QtChart import QChartView, QChart, QBarCategoryAxis
from PyQt5.QtGui import QPainter


class barCharView(QChartView):

    def __init__(self, *args, **kwargs):
        super(barCharView, self).__init__(*args, **kwargs)
        self.setRenderHint(QPainter.Antialiasing)
        self.initChart()

    def initChart(self):
        self._chart = QChart()
        #设置主题
        self._chart.setTheme(QChart.ChartThemeBlueIcy)

        self.setChart(self._chart)