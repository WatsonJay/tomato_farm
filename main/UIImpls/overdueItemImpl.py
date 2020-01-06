# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 17:19
# @Author  : Jaywatson
# @File    : overdueItemImpl.py
# @Soft    : tomato_farm
import datetime

from PyQt5.QtWidgets import QWidget
from UI.overdueListItem import Ui_overdueListItem

class overdueItemImpl(QWidget, Ui_overdueListItem):
    # 初始化
    def __init__(self, parent=None):
        super(overdueItemImpl, self).__init__(parent)
        self.setupUi(self)
        self.taskId = ''

    # 信息填充
    def setInfo(self, data):
        self.taskId = data['id']
        week_day_dict = {
            '0': '星期一',
            '1': '星期二',
            '2': '星期三',
            '3': '星期四',
            '4': '星期五',
            '5': '星期六',
            '6': '星期天',
        }
        week = datetime.datetime.strptime(data['link_date'], "%Y-%m-%d").strftime("%w")
        self.dateLabel.setText(week_day_dict[week]+" "+data['link_date'])
        self.taskNameLabel.setText(data['task_name'],"white")