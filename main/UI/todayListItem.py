# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todayListItem.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_todayListItem(object):
    def setupUi(self, todayListItem):
        todayListItem.setObjectName("todayListItem")
        todayListItem.resize(319, 36)
        todayListItem.setStyleSheet("#todayListItem{\n"
"    background:rgba(255, 255, 255, 0);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(todayListItem)
        self.horizontalLayout.setContentsMargins(9, 3, 1, 3)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radiusLabel = QtWidgets.QLabel(todayListItem)
        self.radiusLabel.setMinimumSize(QtCore.QSize(12, 12))
        self.radiusLabel.setMaximumSize(QtCore.QSize(12, 12))
        self.radiusLabel.setStyleSheet("#radiusLabel{\n"
"    border-radius:6px;\n"
"    background:white;\n"
"}")
        self.radiusLabel.setText("")
        self.radiusLabel.setObjectName("radiusLabel")
        self.horizontalLayout.addWidget(self.radiusLabel)
        self.taskNameLabel = nameLabel(todayListItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.taskNameLabel.setFont(font)
        self.taskNameLabel.setText("")
        self.taskNameLabel.setObjectName("taskNameLabel")
        self.horizontalLayout.addWidget(self.taskNameLabel)
        self.buttonWidget = QtWidgets.QWidget(todayListItem)
        self.buttonWidget.setMaximumSize(QtCore.QSize(100, 16777215))
        self.buttonWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonWidget.setStyleSheet("#buttonWidget>QPushButton{\n"
"    border:none;\n"
"    border-radius:12px;\n"
"}")
        self.buttonWidget.setObjectName("buttonWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.buttonWidget)
        self.horizontalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.topButton = QtWidgets.QPushButton(self.buttonWidget)
        self.topButton.setMinimumSize(QtCore.QSize(24, 24))
        self.topButton.setMaximumSize(QtCore.QSize(24, 24))
        self.topButton.setStyleSheet("#topButton{\n"
"    background:#44AEEE;\n"
"}\n"
"\n"
"#topButton::pressed{\n"
"    background:#2b6f96;\n"
"}")
        self.topButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.topButton.setIcon(icon)
        self.topButton.setIconSize(QtCore.QSize(12, 12))
        self.topButton.setObjectName("topButton")
        self.horizontalLayout_2.addWidget(self.topButton)
        self.startButton = QtWidgets.QPushButton(self.buttonWidget)
        self.startButton.setMinimumSize(QtCore.QSize(24, 24))
        self.startButton.setMaximumSize(QtCore.QSize(24, 24))
        self.startButton.setStyleSheet("#startButton{\n"
"    background:#6CE872;\n"
"}\n"
"\n"
"#startButton::pressed{\n"
"    background:#3c823f;\n"
"}\n"
"")
        self.startButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon1)
        self.startButton.setIconSize(QtCore.QSize(12, 12))
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        self.deleteButton = QtWidgets.QPushButton(self.buttonWidget)
        self.deleteButton.setMinimumSize(QtCore.QSize(24, 24))
        self.deleteButton.setMaximumSize(QtCore.QSize(24, 24))
        self.deleteButton.setStyleSheet("#deleteButton{\n"
"    background:#F95D5C;\n"
"}\n"
"\n"
"#deleteButton::pressed{\n"
"    background:#aa3e3e;\n"
"}")
        self.deleteButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/delete_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon2)
        self.deleteButton.setIconSize(QtCore.QSize(12, 12))
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.horizontalLayout.addWidget(self.buttonWidget)

        self.retranslateUi(todayListItem)
        QtCore.QMetaObject.connectSlotsByName(todayListItem)

    def retranslateUi(self, todayListItem):
        _translate = QtCore.QCoreApplication.translate
        todayListItem.setWindowTitle(_translate("todayListItem", "Form"))
from UI.namelabel import nameLabel
import UI.icons_rc
