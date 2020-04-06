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
        todoWidget.resize(357, 411)
        todoWidget.setWindowTitle("")
        todoWidget.setWindowOpacity(1.0)
        todoWidget.setAutoFillBackground(False)
        todoWidget.setStyleSheet("")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(todoWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.showHideWidget = QtWidgets.QWidget(todoWidget)
        self.showHideWidget.setMinimumSize(QtCore.QSize(30, 90))
        self.showHideWidget.setMaximumSize(QtCore.QSize(30, 90))
        self.showHideWidget.setStyleSheet("QWidget#showHideWidget{\n"
"background:rgba(86, 86, 86, 140);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}")
        self.showHideWidget.setObjectName("showHideWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.showHideWidget)
        self.horizontalLayout_3.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.showHideWidget)
        self.label.setMinimumSize(QtCore.QSize(20, 20))
        self.label.setMaximumSize(QtCore.QSize(20, 20))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addWidget(self.showHideWidget)
        spacerItem = QtWidgets.QSpacerItem(30, 321, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.mainWidget = QtWidgets.QWidget(todoWidget)
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.windowBar = QtWidgets.QWidget(self.mainWidget)
        self.windowBar.setMinimumSize(QtCore.QSize(0, 15))
        self.windowBar.setStyleSheet("QWidget{\n"
"background:rgba(26, 26, 26, 120);\n"
"}")
        self.windowBar.setObjectName("windowBar")
        self.verticalLayout_4.addWidget(self.windowBar)
        self.toolWidget = QtWidgets.QWidget(self.mainWidget)
        self.toolWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.toolWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.toolWidget.setStyleSheet("#toolWidget{\n"
"background:rgba(26, 26, 26, 120);\n"
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
        font.setUnderline(False)
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
        font.setUnderline(False)
        self.changeButton.setFont(font)
        self.changeButton.setStyleSheet("#changeButton{\n"
"    border:none;\n"
"    margin-top:10px;\n"
"    color: rgb(158, 158, 158);\n"
"}")
        self.changeButton.setObjectName("changeButton")
        self.horizontalLayout.addWidget(self.changeButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
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
        self.verticalLayout_4.addWidget(self.toolWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainWidget)
        self.stackedWidget.setStyleSheet("QStackedWidget{\n"
"    background:rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QStackedWidget>QWidget{\n"
"    background:rgba(26, 26, 26, 120);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.todayPage = QtWidgets.QWidget()
        self.todayPage.setObjectName("todayPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.todayPage)
        self.verticalLayout_3.setContentsMargins(3, 6, 3, 6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.todayListWidget = QtWidgets.QListWidget(self.todayPage)
        self.todayListWidget.setStyleSheet("#todayListWidget{\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.todayListWidget.verticalScrollBar().setStyleSheet("QScrollBar{width:0px;}")
        self.todayListWidget.setObjectName("todayListWidget")
        self.verticalLayout_3.addWidget(self.todayListWidget)
        self.stackedWidget.addWidget(self.todayPage)
        self.overduePage = QtWidgets.QWidget()
        self.overduePage.setStyleSheet("")
        self.overduePage.setObjectName("overduePage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.overduePage)
        self.verticalLayout_2.setContentsMargins(3, 6, 3, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.overdueListWidget = QtWidgets.QListWidget(self.overduePage)
        self.overdueListWidget.setStyleSheet("#overdueListWidget{\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.overdueListWidget.verticalScrollBar().setStyleSheet("QScrollBar{width:0px;}")
        self.overdueListWidget.setObjectName("overdueListWidget")
        self.verticalLayout_2.addWidget(self.overdueListWidget)
        self.stackedWidget.addWidget(self.overduePage)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_4.setStretch(2, 9)
        self.horizontalLayout_2.addWidget(self.mainWidget)
        self.horizontalLayout_2.setStretch(1, 9)

        self.retranslateUi(todoWidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(todoWidget)

    def retranslateUi(self, todoWidget):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("todoWidget", "<html><head/><body><p><img src=\":/icon/show.png\" height=\"20\" width=\"20\"/></p></body></html>"))
        self.currentLabel.setText(_translate("todoWidget", "Today"))
        self.changeButton.setText(_translate("todoWidget", "Overdue"))

import UI.icons_rc
