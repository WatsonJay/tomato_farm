# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 11:00
# @Author  : Jaywatson
# @File    : PieChartView.py
# @Soft    : tomato_farm
from PyQt5.QtChart import QChartView, QChart, QPieSeries
from PyQt5.QtCore import QMargins, QPoint
from PyQt5.QtGui import QPainter

from UI.chartToolTip import GraphicsProxyWidget


class pieChartView(QChartView):

    def __init__(self, *args, **kwargs):
        super(pieChartView, self).__init__(*args, **kwargs)
        self.initChart()
        self.refresh()

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
        self._series.setPieSize(0.8)
        self._chart.addSeries(self._series)
        self.setChart(self._chart)

    def refresh(self):
        # 提示widget
        self.toolTipWidget = GraphicsProxyWidget(self._chart)

    def mouseMoveEvent(self, event):
        super(pieChartView, self).mouseMoveEvent(event)
        pos = event.pos()
        x = pos.x()
        y = pos.y()
        # 得到在坐标系中的所有区域
        self.min_x, self.max_x = self._chart.geometry().width()*0.2 , self._chart.geometry().width()*0.8
        self.min_y, self.max_y = self._chart.geometry().height()*0.2 , self._chart.geometry().height()*0.9
        serie = self._chart.series()[0]
        slices = [(slice, slice.value())
                for slice in serie.slices()]
        if self.min_x <=x <= self.max_x and self.min_y <= y <= self.max_y:
            t_width = self.toolTipWidget.width()
            t_height = self.toolTipWidget.height()
            title = "数据组成"
            # 如果鼠标位置离右侧的距离小于tip宽度
            x = pos.x() - t_width if self.width() - \
                                     pos.x() - 20 < t_width else pos.x()
            # 如果鼠标位置离底部的高度小于tip高度
            y = pos.y() - t_height if self.height() - \
                                      pos.y() - 20 < t_height else pos.y()
            self.toolTipWidget.show(
                title, slices, QPoint(x, y))
        else:
            self.toolTipWidget.hide()
