# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unlockDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_unlockDialog(object):
    def setupUi(self, unlockDialog):
        unlockDialog.setObjectName("unlockDialog")
        unlockDialog.resize(266, 178)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.verticalLayout = QtWidgets.QVBoxLayout(unlockDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowBar = QtWidgets.QWidget(unlockDialog)
        self.windowBar.setStyleSheet("QWidget#windowBar{\n"
"background:gray;\n"
"border-top:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"border-top-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"}\n"
"#windowBar>QPushButton{\n"
"border-radius:9px\n"
"}")
        self.windowBar.setObjectName("windowBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.windowBar)
        self.horizontalLayout.setContentsMargins(7, 2, 7, 2)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.miniPushButton = QtWidgets.QPushButton(self.windowBar)
        self.miniPushButton.setMinimumSize(QtCore.QSize(18, 18))
        self.miniPushButton.setMaximumSize(QtCore.QSize(18, 18))
        self.miniPushButton.setStyleSheet("QPushButton{\n"
"    background:#FEE66E;\n"
"}\n"
"QPushButton::hover{\n"
"    background:#c5b355;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#c5b355;\n"
"}\n"
"")
        self.miniPushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/miniShow_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.miniPushButton.setIcon(icon)
        self.miniPushButton.setIconSize(QtCore.QSize(12, 12))
        self.miniPushButton.setObjectName("miniPushButton")
        self.horizontalLayout.addWidget(self.miniPushButton)
        self.closePushButton = QtWidgets.QPushButton(self.windowBar)
        self.closePushButton.setMinimumSize(QtCore.QSize(18, 18))
        self.closePushButton.setMaximumSize(QtCore.QSize(18, 18))
        self.closePushButton.setStyleSheet("QPushButton{\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::hover{\n"
"    background:#aa3e3e;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}\n"
"")
        self.closePushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/close_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closePushButton.setIcon(icon1)
        self.closePushButton.setIconSize(QtCore.QSize(12, 12))
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout.addWidget(self.closePushButton)
        self.verticalLayout.addWidget(self.windowBar)
        self.mainWidget = QtWidgets.QWidget(unlockDialog)
        self.mainWidget.setStyleSheet("QWidget#mainWidget{\n"
"background:#e9eaed;\n"
"border-bottom:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"#mainWidget>QLineEdit{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}")
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_2.setContentsMargins(30, -1, 30, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.mainWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout_2.addWidget(self.passwordLineEdit)
        self.unlockPushButton = QtWidgets.QPushButton(self.mainWidget)
        self.unlockPushButton.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.unlockPushButton.setFont(font)
        self.unlockPushButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:6px;\n"
"    color:white;\n"
"    background:#6CE872;\n"
"}")
        self.unlockPushButton.setObjectName("unlockPushButton")
        self.verticalLayout_2.addWidget(self.unlockPushButton)
        self.verticalLayout.addWidget(self.mainWidget)
        self.verticalLayout.setStretch(1, 9)

        self.retranslateUi(unlockDialog)
        self.closePushButton.clicked.connect(unlockDialog.reject)
        self.miniPushButton.clicked.connect(unlockDialog.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(unlockDialog)

    def retranslateUi(self, unlockDialog):
        _translate = QtCore.QCoreApplication.translate
        unlockDialog.setWindowTitle(_translate("unlockDialog", "Dialog"))
        self.passwordLineEdit.setPlaceholderText(_translate("unlockDialog", "请输入密码"))
        self.unlockPushButton.setText(_translate("unlockDialog", "解锁"))

import UI.icons_rc
