# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 11:00
# @Author  : Jaywatson
# @File    : BarChartView.py
# @Soft    : tomato_farm

from PyQt5.QtChart import QChartView, QChart, QBarCategoryAxis, QBarSeries, QValueAxis, QPercentBarSeries
from PyQt5.QtCore import Qt, QMargins, QPointF, QPoint
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QGraphicsLineItem

from UI.chartToolTip import GraphicsProxyWidget


class barChartView(QChartView):

    def __init__(self, xAxis=[], *args, **kwargs):
        super(barChartView, self).__init__(*args, **kwargs)
        self.initChart(xAxis)

        # line 宽度需要调整
        self.lineItem = QGraphicsLineItem(self._chart)
        pen = QPen(Qt.gray)
        self.lineItem.setPen(pen)
        self.lineItem.setZValue(998)
        self.lineItem.hide()
        self.cal()

    # 一些固定计算，减少mouseMoveEvent中的计算量
    def cal(self):
        # 提示widget
        self.toolTipWidget = GraphicsProxyWidget(self._chart)
        # 获取x和y轴的最小最大值
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        self.category_len = len(axisX.categories())
        self.min_x, self.max_x = -0.5, self.category_len - 0.5
        self.min_y, self.max_y = axisY.min(), axisY.max()
        # 坐标系中左上角顶点
        self.point_top = self._chart.mapToPosition(
            QPointF(self.min_x, self.max_y))

    def setCat(self, data):
        self.categories = data

    #初始化
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
        # chart的图例
        legend = self._chart.legend()
        legend.setVisible(True)

        self.setChart(self._chart)

    def mouseMoveEvent(self, event):
        super(barChartView, self).mouseMoveEvent(event)
        pos = event.pos()
        # 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(pos).x()
        y = self._chart.mapToValue(pos).y()
        index = round(x)
        # 得到在坐标系中的所有bar的类型和点
        serie = self._chart.series()[0]
        bars = [(bar, bar.at(index))
                for bar in serie.barSets() if self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y]
        # print(bars)
        if bars:
            right_top = self._chart.mapToPosition(
                QPointF(self.max_x, self.max_y))
            # 等分距离比例
            step_x = round(
                (right_top.x() - self.point_top.x()) / self.category_len)
            posx = self._chart.mapToPosition(QPointF(x, self.min_y))
            self.lineItem.setLine(posx.x(), self.point_top.y(),
                                  posx.x(), posx.y())
            self.lineItem.show()
            try:
                title = self.categories[index]
            except:
                title = ""
            t_width = self.toolTipWidget.width()
            t_height = self.toolTipWidget.height()
            # 如果鼠标位置离右侧的距离小于tip宽度
            x = pos.x() - t_width if self.width() - \
                pos.x() - 20 < t_width else pos.x()
            # 如果鼠标位置离底部的高度小于tip高度
            y = pos.y() - t_height if self.height() - \
                pos.y() - 20 < t_height else pos.y()
            self.toolTipWidget.show(
                title, bars, QPoint(x, y))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()