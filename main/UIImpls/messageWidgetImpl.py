# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 17:45
# @Author  : Jaywatson
# @File    : messageWidgetImpl.py
# @Soft    : tomato_farm
from PyQt5.QtCore import QPoint, QPropertyAnimation, QTimer, Qt
from PyQt5.QtWidgets import QWidget, QApplication

from UI.messageWidget import Ui_messageWidget
from util.logger import logger


class messageWidgetImpl(QWidget, Ui_messageWidget):
    # 初始化
    def __init__(self, timeout=6000, parent=None):
        super(messageWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        log = logger()
        self.message = log.getlogger('gui')
        self._timeout = timeout
        self._init()

    def _init(self):
        # 是否正在显示标志
        self.isShowing = True
        # 超时
        self._hasFocus = False
        # 桌面对象
        self._desktop = QApplication.desktop()
        current_monitor = self._desktop.screenNumber(self)
        self._desktopGem = self._desktop.availableGeometry(current_monitor)
        # 窗口初始开始位置
        self._startPos = QPoint(
            self._desktopGem.x() + self._desktopGem.width() - self.width() - 5,
            self._desktopGem.y() + self._desktopGem.height()
        )
        # 窗口弹出结束位置
        self._endPos = QPoint(
            self._desktopGem.x() + self._desktopGem.width() - self.width() - 5,
            self._desktopGem.y() + self._desktopGem.height() - self.height() - 5
        )
        # 初始化位置到右下角
        self.move(self._startPos)
        # 动画
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.finished.connect(self.onAnimationEnd)
        self.animation.setDuration(2000)  # 2s
        # 弹回定时器
        self._timer = QTimer(self, timeout=self.closeAnimation)

    def show(self, content=''):
        self._timer.stop()  # 停止定时器
        self.hide()
        self.move(self._startPos)
        self.setContent(content)
        super(messageWidgetImpl, self).show()
        return self

    #显示动画
    def showAnimation(self):
        self.message.debug('showAnimation')
        self.isShowing = True
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._endPos)
        self.animation.start()
        self._timer.start(self._timeout)

    # 关闭动画
    def closeAnimation(self):
        self.message.debug('closeAnimation')
        # 关闭动画
        if self.hasFocus():
            # 如果弹出后倒计时5秒后还有焦点存在则失去焦点后需要主动触发关闭
            self._hasFocus = True
            return  # 如果有焦点则不关闭
        self.isShowing = False
        self.animation.stop()
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(self._startPos)
        self.animation.start()

    # 动画结束
    def onAnimationEnd(self):
        if not self.isShowing:
            self.message.debug("onAnimationEnd close()")
            self.close()
            self.message.debug("onAnimationEnd stop timer")
            self._timer.stop()

    def enterEvent(self, QEvent):
        self.message.debug("enterEvent setFocus Qt.MouseFocusReason")
        self.setFocus(Qt.MouseFocusReason)

    def leaveEvent(self, QEvent):
        self.message.debug("leaveEvent clearFocus")
        self.clearFocus()
        if self._hasFocus:
            QTimer.start(1000, self.closeAnimation)

    def setContent(self, content):
        if content:
            self.label.setText(content)

    def content(self):
        return self.label.text()

    def setTimeout(self, timeout):
        if isinstance(timeout, int):
            self._timeout = timeout
        return self

    def timeout(self):
        return self._timeout