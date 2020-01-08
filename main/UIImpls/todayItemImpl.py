# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 17:20
# @Author  : Jaywatson
# @File    : todayItemImpl.py
# @Soft    : tomato_farm
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from UI.todayListItem import Ui_todayListItem

class todayItemImpl(QWidget, Ui_todayListItem):

    taskRefreshSignal = pyqtSignal()

    # 初始化
    def __init__(self, parent=None):
        super(todayItemImpl, self).__init__(parent)
        self.setupUi(self)
        self.taskId = ''

    # 信息填充
    def setInfo(self, data):
        if data['is_top'] == 1:
            self.radiusLabel.setStyleSheet("#radiusLabel{border-radius:6px;background:#FEE66E;}")
        self.taskNameLabel.setText(data['task_name'],"white")

    # 任务置顶
    def topTask(self):
        try:
            sql = "Update t_task_link_date set is_doing = 0 where task_id = ?"
            self.sqlite.execute(sql, self.task['id'])
            self.taskRefreshSignal.emit()
            self.task = {}
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmain.error(e)