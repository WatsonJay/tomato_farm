# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskItem.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_taskItem(object):
    def setupUi(self, taskItem):
        taskItem.setObjectName("taskItem")
        taskItem.resize(381, 50)
        taskItem.setMinimumSize(QtCore.QSize(381, 50))
        taskItem.setMaximumSize(QtCore.QSize(381, 50))
        taskItem.setSizeIncrement(QtCore.QSize(0, 0))
        taskItem.setBaseSize(QtCore.QSize(0, 0))
        taskItem.setStyleSheet("#taskItem{\n"
"    background-color: rgba(173, 173, 173, 120);\n"
"    border-bottom:1px solid gray;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(taskItem)
        self.verticalLayout.setContentsMargins(-1, 3, -1, 3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(taskItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.taskNameLabel = QtWidgets.QLabel(taskItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.taskNameLabel.setFont(font)
        self.taskNameLabel.setText("")
        self.taskNameLabel.setObjectName("taskNameLabel")
        self.horizontalLayout.addWidget(self.taskNameLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.typeLabel = QtWidgets.QLabel(taskItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.typeLabel.setFont(font)
        self.typeLabel.setText("")
        self.typeLabel.setObjectName("typeLabel")
        self.horizontalLayout.addWidget(self.typeLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(taskItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.yearLabel = QtWidgets.QLabel(taskItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.yearLabel.setFont(font)
        self.yearLabel.setObjectName("yearLabel")
        self.horizontalLayout_2.addWidget(self.yearLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(taskItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.duringTimeLabel = QtWidgets.QLabel(taskItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.duringTimeLabel.setFont(font)
        self.duringTimeLabel.setObjectName("duringTimeLabel")
        self.horizontalLayout_2.addWidget(self.duringTimeLabel)
        self.label_7 = QtWidgets.QLabel(taskItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(taskItem)
        QtCore.QMetaObject.connectSlotsByName(taskItem)

    def retranslateUi(self, taskItem):
        _translate = QtCore.QCoreApplication.translate
        taskItem.setWindowTitle(_translate("taskItem", "Form"))
        self.label.setText(_translate("taskItem", "任务名："))
        self.label_2.setText(_translate("taskItem", "截至时间："))
        self.yearLabel.setText(_translate("taskItem", "0000-00-00"))
        self.label_5.setText(_translate("taskItem", "时长："))
        self.duringTimeLabel.setText(_translate("taskItem", "0"))
        self.label_7.setText(_translate("taskItem", "分钟"))

