# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 22:37
# @Author  : Jaywatson
# @File    : namelabel.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class nameLabel(QLabel):
    def __init__(self, parent=None):
        super(nameLabel, self).__init__(parent)
        self.txt=''
        self.newX = 0
        self.color = 'black'
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.changeTxtPosition)

    def changeTxtPosition(self):
        if not self.parent().isVisible():
            self.t.stop()
            self.newX = 0
            return
        if self.textRect.width() + self.newX > 0:
            self.newX -= 5
        else:
            self.newX = self.width()
        self.update()

    def setText(self,txt,color='black'):
        self.txt = txt
        self.color = color
        self.newX = 0
        self.update()

    def enterEvent(self, event):
        self.timer.start(500)

    def leaveEvent(self, event):
        # 鼠标离开则停止滚动并复位
        self.timer.stop()
        self.newX = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor('transparent'))
        self.textRect = painter.drawText(QRect(0, 0, self.width(), self.height()), Qt.AlignLeft | Qt.AlignVCenter, self.txt)

        if self.textRect.width() > self.width():
            painter.setPen(QColor(self.color)) # 黑色
            painter.drawText(QRect(self.newX, 0, self.textRect.width(), self.height()), Qt.AlignLeft | Qt.AlignVCenter, self.txt)
        else:
            painter.setPen(QColor(self.color))  # 黑色
            painter.drawText(QRect(0, 0, self.width(), self.height()), Qt.AlignLeft | Qt.AlignVCenter, self.txt)
            self.timer.stop()

