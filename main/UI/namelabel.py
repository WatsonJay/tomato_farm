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
        self.timer = QTimer(self)
        self.font = QFont('Microsoft YaHei UI', 10)
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

    def setText(self,s):
        self.txt = s
        self.newX = 0
        self.update()

    def enterEvent(self, event):
        self.timer.start(150)

    def leaveEvent(self, event):
        # 鼠标离开则停止滚动并复位
        self.timer.stop()
        self.newX = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(self.font)
        #painter.setPen(QColor('transparent'));
        self.textRect = painter.drawText(QRect(0, 0, self.width(), self.height()), Qt.AlignHCenter | Qt.AlignVCenter, self.txt)

        if self.textRect.width() > self.width():
            #painter.setPen(QColor('black'));  # 黑色
            painter.drawText(QRect(self.newX, 0, self.textRect.width(), self.height()), Qt.AlignLeft | Qt.AlignVCenter, self.txt)
        else:
            #painter.setPen(QColor('black'));  # 黑色
            self.textRect = painter.drawText(QRect(0, 0, self.width(), self.height()), Qt.AlignLeft | Qt.AlignVCenter, self.txt)
            self.timer.stop()

