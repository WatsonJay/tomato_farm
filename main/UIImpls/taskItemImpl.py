# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 12:19
# @Author  : Jaywatson
# @File    : taskItemImpl.py
# @Soft    : tomato_farm
import datetime

from PyQt5.QtWidgets import QWidget

from UI.taskItem import Ui_taskItem

class taskItemImpl(QWidget, Ui_taskItem):
    # 初始化
    def __init__(self, parent=None):
        super(taskItemImpl, self).__init__(parent)
        self.setupUi(self)
        self.taskId = ''
        self.during = 0

    def setInfo(self,data):
        self.taskId = data['id']
        self.taskNameLabel.setText(data['task_name'])
        self.during = data['task_during']
        self.duringTimeLabel.setText(str(data['task_during']))
        deadline = datetime.datetime.strptime(data['deadline_time'],"%Y-%m-%d")
        now = datetime.datetime.now() + datetime.timedelta(days=-1)
        if deadline < now:
            self.yearLabel.setText("<font color=%s>%s</font>" % ('#F95D5C', data['deadline_time']))
        else:
            self.yearLabel.setText("<font color=%s>%s</font>" % ("black", data['deadline_time']))
        if data['is_overdue'] == 1 and data['is_finish'] == 0:
            self.typeLabel.setText("<font color=%s>%s</font>" % ('#F95D5C', "已逾期"))
        if data['is_finish'] == 1:
            self.typeLabel.setText("<font color=%s>%s</font>" % ('#6CE872', "已完成"))
        if data['is_overdue'] == 0 and data['is_dated'] == 1:
            self.typeLabel.setText("<font color=%s>%s</font>" % ('#F95D5C', "已分配"))