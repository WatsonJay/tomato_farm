# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 22:46
# @Author  : Jaywatson
# @File    : noBorderImpl.py
# @Soft    : tomato_farm
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor

class noBorderImpl:

    # 无边框移动窗体
    def mousePressEvent(self, QMouseEvent):
        try:
            if QMouseEvent.button() == QtCore.Qt.LeftButton:
                self.flag = True
                self.m_Position = QMouseEvent.globalPos() - self.pos()
                QMouseEvent.accept()
                self.setCusor(QCursor(QtCore.Qt.OpenHandCursor))
        except Exception as e:
            pass

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.flag = False
        self.setCursor(QCursor(QtCore.Qt.ArrowCursor))