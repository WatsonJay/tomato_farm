# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 22:46
# @Author  : Jaywatson
# @File    : noBorderImpl.py
# @Soft    : tomato_farm
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QEnterEvent
from PyQt5.QtWidgets import QMessageBox

from util.logger import logger


class noBorderImpl:

    log = logger()
    confnoborder = log.getlogger('gui')
    flag = False

    # 无边框移动窗体
    def mousePressEvent(self, QMouseEvent):
        try:
            if QMouseEvent.button() == QtCore.Qt.LeftButton:
                self.flag = True
                self.m_Position = QMouseEvent.globalPos() - self.pos()
                self.setCursor(QtCore.Qt.ClosedHandCursor)
                QMouseEvent.accept()
        except Exception as e:
            self.confnoborder.error(e)
            pass

    def mouseMoveEvent(self, QMouseEvent):
        try:
            if QtCore.Qt.LeftButton and self.flag:
                self.move(QMouseEvent.globalPos() - self.m_Position)
                QMouseEvent.accept()
        except Exception as e:
            self.confnoborder.error(e)
            pass

    def mouseReleaseEvent(self, QMouseEvent):
        try:
            self.flag = False
            self.setCursor(QtCore.Qt.ArrowCursor)
        except Exception as e:
            self.confnoborder.error(e)
            pass