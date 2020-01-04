# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'miniBar.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_miniBarForm(object):
    def setupUi(self, miniBarForm):
        miniBarForm.setObjectName("miniBarForm")
        miniBarForm.resize(304, 127)
        miniBarForm.setWindowTitle("")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.verticalLayout = QtWidgets.QVBoxLayout(miniBarForm)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowBar = QtWidgets.QWidget(miniBarForm)
        self.windowBar.setStyleSheet("QWidget#windowBar{\n"
"background:rgba(100, 100, 100, 120);\n"
"border-top-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"border-top:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"}")
        self.windowBar.setObjectName("windowBar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.windowBar)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout.addWidget(self.windowBar)
        self.mainWindow = QtWidgets.QWidget(miniBarForm)
        self.mainWindow.setStyleSheet("QWidget#mainWindow{\n"
"background:rgba(100, 100, 100, 120);\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"border-bottom:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"}")
        self.mainWindow.setObjectName("mainWindow")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainWindow)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.mainWindow)
        self.label_3.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.taskLabel = nameLabel(self.mainWindow)
        self.taskLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.taskLabel.setStyleSheet("color:white;")
        self.taskLabel.setText("")
        self.taskLabel.setObjectName("taskLabel")
        self.horizontalLayout_2.addWidget(self.taskLabel)
        self.label = QtWidgets.QLabel(self.mainWindow)
        self.label.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.tomatoStageLabel = QtWidgets.QLabel(self.mainWindow)
        self.tomatoStageLabel.setMinimumSize(QtCore.QSize(30, 0))
        self.tomatoStageLabel.setStyleSheet("color:white;")
        self.tomatoStageLabel.setText("")
        self.tomatoStageLabel.setObjectName("tomatoStageLabel")
        self.horizontalLayout_2.addWidget(self.tomatoStageLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeBar = QtWidgets.QProgressBar(self.mainWindow)
        self.timeBar.setStyleSheet("#timeBar{\n"
"    color: rgb(244, 98, 98);\n"
"    border-radius:6px;\n"
"    border: 1px solid #808080;\n"
"}\n"
"#timeBar::chunk{\n"
"    border-radius:3px;\n"
"       width:6px;\n"
"    background-color:#F95D5C;\n"
"       margin:0.5px;\n"
"\n"
"}")
        self.timeBar.setProperty("value", 0)
        self.timeBar.setTextVisible(False)
        self.timeBar.setInvertedAppearance(False)
        self.timeBar.setObjectName("timeBar")
        self.horizontalLayout.addWidget(self.timeBar)
        self.timeLcd = QtWidgets.QLCDNumber(self.mainWindow)
        self.timeLcd.setStyleSheet("border:none;")
        self.timeLcd.setSmallDecimalPoint(True)
        self.timeLcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.timeLcd.setObjectName("timeLcd")
        self.horizontalLayout.addWidget(self.timeLcd)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.redoButton = QtWidgets.QPushButton(self.mainWindow)
        self.redoButton.setMinimumSize(QtCore.QSize(30, 30))
        self.redoButton.setMaximumSize(QtCore.QSize(30, 30))
        self.redoButton.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}\n"
"")
        self.redoButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon)
        self.redoButton.setObjectName("redoButton")
        self.horizontalLayout_3.addWidget(self.redoButton)
        self.playButton = QtWidgets.QPushButton(self.mainWindow)
        self.playButton.setMinimumSize(QtCore.QSize(30, 30))
        self.playButton.setMaximumSize(QtCore.QSize(30, 30))
        self.playButton.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}\n"
"")
        self.playButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon1)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_3.addWidget(self.playButton)
        self.pazueButton = QtWidgets.QPushButton(self.mainWindow)
        self.pazueButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pazueButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pazueButton.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}\n"
"")
        self.pazueButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pazueButton.setIcon(icon2)
        self.pazueButton.setObjectName("pazueButton")
        self.horizontalLayout_3.addWidget(self.pazueButton)
        self.stopButton = QtWidgets.QPushButton(self.mainWindow)
        self.stopButton.setMinimumSize(QtCore.QSize(30, 30))
        self.stopButton.setMaximumSize(QtCore.QSize(30, 30))
        self.stopButton.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}\n"
"")
        self.stopButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon3)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_3.addWidget(self.stopButton)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.normalSizeButton = QtWidgets.QPushButton(self.mainWindow)
        self.normalSizeButton.setMinimumSize(QtCore.QSize(22, 22))
        self.normalSizeButton.setMaximumSize(QtCore.QSize(22, 22))
        self.normalSizeButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#565656;\n"
"}")
        self.normalSizeButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/normalWindow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.normalSizeButton.setIcon(icon4)
        self.normalSizeButton.setIconSize(QtCore.QSize(20, 20))
        self.normalSizeButton.setObjectName("normalSizeButton")
        self.horizontalLayout_3.addWidget(self.normalSizeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout.addWidget(self.mainWindow)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)

        self.retranslateUi(miniBarForm)
        QtCore.QMetaObject.connectSlotsByName(miniBarForm)

    def retranslateUi(self, miniBarForm):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("miniBarForm", "任务："))
        self.label.setText(_translate("miniBarForm", "状态："))

from UI.namelabel import nameLabel
import UI.icons_rc
