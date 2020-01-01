# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 21:46
# @Author  : Jaywatson
# @File    : taskRunThread.py
# @Soft    : tomato_farm

from PyQt5.QtCore import QThread, pyqtSignal

class taskRunThread(QThread):
    sendMsgSignal = pyqtSignal(dict)

    def __init__(self,id='',during=0):
        super().__init__()
        self.taskId = id
        self.taskDuring = during