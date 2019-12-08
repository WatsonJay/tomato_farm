# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todoWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_todoWidget(object):
    def setupUi(self, todoWidget):
        todoWidget.setObjectName("todoWidget")
        todoWidget.resize(333, 409)
        todoWidget.setWindowTitle("")
        todoWidget.setWindowOpacity(1.0)
        todoWidget.setAutoFillBackground(False)
        todoWidget.setStyleSheet("")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.verticalLayout = QtWidgets.QVBoxLayout(todoWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowBar = QtWidgets.QWidget(todoWidget)
        self.windowBar.setMinimumSize(QtCore.QSize(0, 15))
        self.windowBar.setStyleSheet("QWidget#windowBar{\n"
"background:rgba(100, 100, 100, 120);\n"
"border-top:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"}")
        self.windowBar.setObjectName("windowBar")
        self.verticalLayout.addWidget(self.windowBar)
        self.toolWidget = QtWidgets.QWidget(todoWidget)
        self.toolWidget.setStyleSheet("QWidget#toolWidget{\n"
"background:rgba(100, 100, 100, 120);\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"}")
        self.toolWidget.setObjectName("toolWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolWidget)
        self.horizontalLayout.setContentsMargins(9, 0, -1, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.currentLabel = QtWidgets.QLabel(self.toolWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.currentLabel.setFont(font)
        self.currentLabel.setStyleSheet("#currentLabel{\n"
"    color:white;\n"
"}")
        self.currentLabel.setObjectName("currentLabel")
        self.horizontalLayout.addWidget(self.currentLabel)
        self.changeButton = QtWidgets.QPushButton(self.toolWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setUnderline(True)
        self.changeButton.setFont(font)
        self.changeButton.setStyleSheet("#changeButton{\n"
"    border:none;\n"
"    margin-top:10px;\n"
"    color: #5f5f5f;\n"
"}")
        self.changeButton.setObjectName("changeButton")
        self.horizontalLayout.addWidget(self.changeButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lockButton = QtWidgets.QPushButton(self.toolWidget)
        self.lockButton.setMinimumSize(QtCore.QSize(30, 30))
        self.lockButton.setMaximumSize(QtCore.QSize(30, 30))
        self.lockButton.setStyleSheet("#lockButton{\n"
"    border:none;\n"
"}")
        self.lockButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lockButton.setIcon(icon)
        self.lockButton.setIconSize(QtCore.QSize(30, 30))
        self.lockButton.setObjectName("lockButton")
        self.horizontalLayout.addWidget(self.lockButton)
        self.verticalLayout.addWidget(self.toolWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(todoWidget)
        self.stackedWidget.setStyleSheet("QStackedWidget{\n"
"background:rgba(255, 255, 255, 0);\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"border-bottom:1px solid gray;\n"
"}\n"
"QStackedWidget>QWidget{\n"
"background:rgba(100, 100, 100, 120);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.todayPage = QtWidgets.QWidget()
        self.todayPage.setObjectName("todayPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.todayPage)
        self.verticalLayout_3.setContentsMargins(3, 0, 3, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.todayListWidget = QtWidgets.QListWidget(self.todayPage)
        self.todayListWidget.setStyleSheet("#todayListWidget{\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.todayListWidget.setObjectName("todayListWidget")
        self.verticalLayout_3.addWidget(self.todayListWidget)
        self.stackedWidget.addWidget(self.todayPage)
        self.overduePage = QtWidgets.QWidget()
        self.overduePage.setStyleSheet("#overdueListWidget{\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.overduePage.setObjectName("overduePage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.overduePage)
        self.verticalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.overdueListWidget = QtWidgets.QListWidget(self.overduePage)
        self.overdueListWidget.setObjectName("overdueListWidget")
        self.verticalLayout_2.addWidget(self.overdueListWidget)
        self.stackedWidget.addWidget(self.overduePage)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 6)

        self.retranslateUi(todoWidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(todoWidget)

    def retranslateUi(self, todoWidget):
        _translate = QtCore.QCoreApplication.translate
        self.currentLabel.setText(_translate("todoWidget", "Today"))
        self.changeButton.setText(_translate("todoWidget", "Overdue"))

import UI.icons_rc
