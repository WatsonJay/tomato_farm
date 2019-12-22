# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messageWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messageWidget(object):
    def setupUi(self, messageWidget):
        messageWidget.setObjectName("messageWidget")
        messageWidget.resize(306, 216)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(messageWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleWidget = QtWidgets.QWidget(messageWidget)
        self.titleWidget.setMinimumSize(QtCore.QSize(0, 20))
        self.titleWidget.setStyleSheet("#titleWidget{\n"
"    border:none;\n"
"    background:rgba(249, 93, 92, 200);\n"
"    border-top-right-radius:7px;\n"
"    border-top-left-radius:7px;\n"
"}")
        self.titleWidget.setObjectName("titleWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.titleWidget)
        self.horizontalLayout_2.setContentsMargins(7, 2, 7, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.titleWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_2.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/close_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.titleWidget)
        self.contextWidget = QtWidgets.QWidget(messageWidget)
        self.contextWidget.setStyleSheet("#contextWidget{\n"
"    background:rgba(233, 234, 237, 200);\n"
"    border-left:1px solid gray;;\n"
"    border-right:1px solid gray;;\n"
"}")
        self.contextWidget.setObjectName("contextWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.contextWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.contextWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.contextWidget)
        self.bottomWidget = QtWidgets.QWidget(messageWidget)
        self.bottomWidget.setStyleSheet("QWidget{\n"
"    background:rgba(233, 234, 237, 200);\n"
"    border:1px solid gray;\n"
"    border-top:2px solid gray;\n"
"}")
        self.bottomWidget.setObjectName("bottomWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottomWidget)
        self.horizontalLayout.setContentsMargins(-1, 9, -1, 9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.bottomWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 20))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    color:white;\n"
"    border-radius:10px;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#aa3e3e;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#aa3e3e;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.bottomWidget)
        self.verticalLayout_2.setStretch(1, 9)

        self.retranslateUi(messageWidget)
        QtCore.QMetaObject.connectSlotsByName(messageWidget)

    def retranslateUi(self, messageWidget):
        _translate = QtCore.QCoreApplication.translate
        messageWidget.setWindowTitle(_translate("messageWidget", "Form"))
        self.pushButton.setText(_translate("messageWidget", "确定"))

import UI.icons_rc
