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
        messageWidget.resize(306, 209)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
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
        self.closeButton = QtWidgets.QPushButton(self.titleWidget)
        self.closeButton.setMinimumSize(QtCore.QSize(18, 18))
        self.closeButton.setMaximumSize(QtCore.QSize(18, 18))
        self.closeButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}")
        self.closeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/close_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(12, 12))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.verticalLayout_2.addWidget(self.titleWidget)
        self.contextWidget = QtWidgets.QWidget(messageWidget)
        self.contextWidget.setStyleSheet("#contextWidget{\n"
"    background:rgba(233, 234, 237, 200);\n"
"    border-left:1px solid gray;;\n"
"    border-right:1px solid gray;;\n"
"}")
        self.contextWidget.setObjectName("contextWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.contextWidget)
        self.verticalLayout.setContentsMargins(20, 15, 20, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.contextWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.contextWidget)
        self.verticalLayout_2.setStretch(1, 9)

        self.retranslateUi(messageWidget)
        QtCore.QMetaObject.connectSlotsByName(messageWidget)

    def retranslateUi(self, messageWidget):
        _translate = QtCore.QCoreApplication.translate
        messageWidget.setWindowTitle(_translate("messageWidget", "Form"))
import UI.icons_rc
