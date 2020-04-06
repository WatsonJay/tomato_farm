# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        MainWindow.resize(989, 633)
        MainWindow.setMinimumSize(QtCore.QSize(989, 633))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowBar = QtWidgets.QWidget(self.centralwidget)
        self.windowBar.setStyleSheet("QWidget#windowBar{\n"
"background:gray;\n"
"border-top:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"border-top-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"}\n"
"#windowBar>QPushButton{\n"
"border-radius:8px\n"
"}")
        self.windowBar.setObjectName("windowBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.windowBar)
        self.horizontalLayout.setContentsMargins(7, 2, 7, 2)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(715, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.miniPushButton = QtWidgets.QPushButton(self.windowBar)
        self.miniPushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.miniPushButton.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.miniPushButton.setFont(font)
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
        self.miniPushButton.setIconSize(QtCore.QSize(10, 10))
        self.miniPushButton.setObjectName("miniPushButton")
        self.horizontalLayout.addWidget(self.miniPushButton)
        self.closePushButton = QtWidgets.QPushButton(self.windowBar)
        self.closePushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.closePushButton.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.closePushButton.setFont(font)
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
        self.closePushButton.setIconSize(QtCore.QSize(10, 10))
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout.addWidget(self.closePushButton)
        self.verticalLayout.addWidget(self.windowBar)
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setStyleSheet("QWidget#mainWidget{\n"
"background:#e9eaed;\n"
"border-bottom:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}")
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_2.setContentsMargins(1, 0, 1, 1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolWidget = QtWidgets.QWidget(self.mainWidget)
        self.toolWidget.setMinimumSize(QtCore.QSize(99, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.toolWidget.setFont(font)
        self.toolWidget.setStyleSheet("#toolWidget{\n"
"    background:#dedede;\n"
"    border-right:1px solid #6d6d6d;\n"
"}\n"
"#toolWidget>QPushButton{\n"
"    border:none;\n"
"}\n"
"#toolWidget>QPushButton:hover{\n"
"    background:#c0d5d6;\n"
"}\n"
"#toolWidget>QPushButton:checked{\n"
"    border-left:2px solid red;\n"
"    background:#c0d5d6;\n"
"}")
        self.toolWidget.setObjectName("toolWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.toolWidget)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(1, 5, 1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.firstPageButton = QtWidgets.QPushButton(self.toolWidget)
        self.firstPageButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.firstPageButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/home_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstPageButton.setIcon(icon2)
        self.firstPageButton.setCheckable(True)
        self.firstPageButton.setAutoExclusive(True)
        self.firstPageButton.setFlat(False)
        self.firstPageButton.setObjectName("firstPageButton")
        self.verticalLayout_3.addWidget(self.firstPageButton)
        self.statisButton = QtWidgets.QPushButton(self.toolWidget)
        self.statisButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.statisButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/stati.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statisButton.setIcon(icon3)
        self.statisButton.setCheckable(True)
        self.statisButton.setAutoExclusive(True)
        self.statisButton.setObjectName("statisButton")
        self.verticalLayout_3.addWidget(self.statisButton)
        self.taskButton = QtWidgets.QPushButton(self.toolWidget)
        self.taskButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.taskButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/task.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.taskButton.setIcon(icon4)
        self.taskButton.setCheckable(True)
        self.taskButton.setAutoExclusive(True)
        self.taskButton.setObjectName("taskButton")
        self.verticalLayout_3.addWidget(self.taskButton)
        self.memoButton = QtWidgets.QPushButton(self.toolWidget)
        self.memoButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.memoButton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/dialog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.memoButton.setIcon(icon5)
        self.memoButton.setCheckable(True)
        self.memoButton.setChecked(False)
        self.memoButton.setAutoExclusive(True)
        self.memoButton.setObjectName("memoButton")
        self.verticalLayout_3.addWidget(self.memoButton)
        self.marketButton = QtWidgets.QPushButton(self.toolWidget)
        self.marketButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.marketButton.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/market.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.marketButton.setIcon(icon6)
        self.marketButton.setCheckable(True)
        self.marketButton.setAutoExclusive(True)
        self.marketButton.setObjectName("marketButton")
        self.verticalLayout_3.addWidget(self.marketButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settingButton = QtWidgets.QPushButton(self.toolWidget)
        self.settingButton.setMinimumSize(QtCore.QSize(25, 25))
        self.settingButton.setMaximumSize(QtCore.QSize(25, 25))
        self.settingButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#c0d5d6;\n"
"}")
        self.settingButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingButton.setIcon(icon7)
        self.settingButton.setObjectName("settingButton")
        self.horizontalLayout_2.addWidget(self.settingButton)
        self.introButton = QtWidgets.QPushButton(self.toolWidget)
        self.introButton.setMinimumSize(QtCore.QSize(25, 25))
        self.introButton.setMaximumSize(QtCore.QSize(25, 25))
        self.introButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#c0d5d6;\n"
"}")
        self.introButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.introButton.setIcon(icon8)
        self.introButton.setObjectName("introButton")
        self.horizontalLayout_2.addWidget(self.introButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.toolWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainWidget)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.DoingWidget = QtWidgets.QWidget(self.mainWidget)
        self.DoingWidget.setStyleSheet("#DoingWidget{\n"
"    border-top:1px solid #6d6d6d;\n"
"}")
        self.DoingWidget.setObjectName("DoingWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.DoingWidget)
        self.horizontalLayout_4.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tomatoPicLabel = QtWidgets.QLabel(self.DoingWidget)
        self.tomatoPicLabel.setMinimumSize(QtCore.QSize(65, 65))
        self.tomatoPicLabel.setMaximumSize(QtCore.QSize(65, 65))
        self.tomatoPicLabel.setText("")
        self.tomatoPicLabel.setObjectName("tomatoPicLabel")
        self.horizontalLayout_4.addWidget(self.tomatoPicLabel)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 13)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(4, 1, -1, 1)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.DoingWidget)
        self.label_2.setMinimumSize(QtCore.QSize(87, 0))
        self.label_2.setMaximumSize(QtCore.QSize(87, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.taskTitleLabel = nameLabel(self.DoingWidget)
        self.taskTitleLabel.setMinimumSize(QtCore.QSize(300, 0))
        self.taskTitleLabel.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.taskTitleLabel.setFont(font)
        self.taskTitleLabel.setText("")
        self.taskTitleLabel.setWordWrap(False)
        self.taskTitleLabel.setObjectName("taskTitleLabel")
        self.horizontalLayout_5.addWidget(self.taskTitleLabel)
        self.label_4 = QtWidgets.QLabel(self.DoingWidget)
        self.label_4.setMinimumSize(QtCore.QSize(64, 0))
        self.label_4.setMaximumSize(QtCore.QSize(64, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.readyTomatoLabel = QtWidgets.QLabel(self.DoingWidget)
        self.readyTomatoLabel.setMaximumSize(QtCore.QSize(26, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.readyTomatoLabel.setFont(font)
        self.readyTomatoLabel.setText("")
        self.readyTomatoLabel.setObjectName("readyTomatoLabel")
        self.horizontalLayout_5.addWidget(self.readyTomatoLabel)
        self.label_6 = QtWidgets.QLabel(self.DoingWidget)
        self.label_6.setMinimumSize(QtCore.QSize(10, 0))
        self.label_6.setMaximumSize(QtCore.QSize(10, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.totalTomatoLabel = QtWidgets.QLabel(self.DoingWidget)
        self.totalTomatoLabel.setMaximumSize(QtCore.QSize(26, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.totalTomatoLabel.setFont(font)
        self.totalTomatoLabel.setText("")
        self.totalTomatoLabel.setObjectName("totalTomatoLabel")
        self.horizontalLayout_5.addWidget(self.totalTomatoLabel)
        self.label_8 = QtWidgets.QLabel(self.DoingWidget)
        self.label_8.setMinimumSize(QtCore.QSize(62, 0))
        self.label_8.setMaximumSize(QtCore.QSize(62, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.tomatoStageLabel = QtWidgets.QLabel(self.DoingWidget)
        self.tomatoStageLabel.setMaximumSize(QtCore.QSize(67, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.tomatoStageLabel.setFont(font)
        self.tomatoStageLabel.setText("")
        self.tomatoStageLabel.setObjectName("tomatoStageLabel")
        self.horizontalLayout_5.addWidget(self.tomatoStageLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.timeBar = QtWidgets.QProgressBar(self.DoingWidget)
        self.timeBar.setStyleSheet("#timeBar{\n"
"    color: rgb(244, 98, 98);\n"
"    border-radius:6px;\n"
"    border: 1px solid #808080;\n"
"}\n"
"#timeBar::chunk{\n"
"    border-radius:3px;\n"
"       width:10px;\n"
"    background-color:#F95D5C;\n"
"       margin:0.5px;\n"
"\n"
"}")
        self.timeBar.setProperty("value", 0)
        self.timeBar.setTextVisible(False)
        self.timeBar.setOrientation(QtCore.Qt.Horizontal)
        self.timeBar.setObjectName("timeBar")
        self.horizontalLayout_6.addWidget(self.timeBar)
        self.timeLcd = QtWidgets.QLCDNumber(self.DoingWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(False)
        font.setWeight(50)
        self.timeLcd.setFont(font)
        self.timeLcd.setStyleSheet("#timeLcd{\n"
"    border:none;\n"
"}")
        self.timeLcd.setSmallDecimalPoint(False)
        self.timeLcd.setDigitCount(5)
        self.timeLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.timeLcd.setProperty("intValue", 0)
        self.timeLcd.setObjectName("timeLcd")
        self.horizontalLayout_6.addWidget(self.timeLcd)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.redoTimerButton = QtWidgets.QPushButton(self.DoingWidget)
        self.redoTimerButton.setMinimumSize(QtCore.QSize(36, 36))
        self.redoTimerButton.setMaximumSize(QtCore.QSize(36, 36))
        self.redoTimerButton.setStyleSheet("QPushButton{\n"
"    border-radius:18px;\n"
"    border:none;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}")
        self.redoTimerButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoTimerButton.setIcon(icon9)
        self.redoTimerButton.setObjectName("redoTimerButton")
        self.horizontalLayout_4.addWidget(self.redoTimerButton)
        self.startTimerButton = QtWidgets.QPushButton(self.DoingWidget)
        self.startTimerButton.setMinimumSize(QtCore.QSize(46, 46))
        self.startTimerButton.setMaximumSize(QtCore.QSize(46, 46))
        self.startTimerButton.setStyleSheet("QPushButton{\n"
"    border-radius:23px;\n"
"    border:none;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}")
        self.startTimerButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startTimerButton.setIcon(icon10)
        self.startTimerButton.setIconSize(QtCore.QSize(24, 24))
        self.startTimerButton.setObjectName("startTimerButton")
        self.horizontalLayout_4.addWidget(self.startTimerButton)
        self.pauseTimerButton = QtWidgets.QPushButton(self.DoingWidget)
        self.pauseTimerButton.setMinimumSize(QtCore.QSize(36, 36))
        self.pauseTimerButton.setMaximumSize(QtCore.QSize(36, 36))
        self.pauseTimerButton.setStyleSheet("QPushButton{\n"
"    border-radius:18px;\n"
"    border:none;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}")
        self.pauseTimerButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseTimerButton.setIcon(icon11)
        self.pauseTimerButton.setObjectName("pauseTimerButton")
        self.horizontalLayout_4.addWidget(self.pauseTimerButton)
        self.stopTimerButton = QtWidgets.QPushButton(self.DoingWidget)
        self.stopTimerButton.setMinimumSize(QtCore.QSize(36, 36))
        self.stopTimerButton.setMaximumSize(QtCore.QSize(36, 36))
        self.stopTimerButton.setStyleSheet("QPushButton{\n"
"    border-radius:18px;\n"
"    border:none;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}")
        self.stopTimerButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopTimerButton.setIcon(icon12)
        self.stopTimerButton.setObjectName("stopTimerButton")
        self.horizontalLayout_4.addWidget(self.stopTimerButton)
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.miniSizeButton = QtWidgets.QPushButton(self.DoingWidget)
        self.miniSizeButton.setMinimumSize(QtCore.QSize(25, 25))
        self.miniSizeButton.setMaximumSize(QtCore.QSize(25, 25))
        self.miniSizeButton.setStyleSheet("#miniSizeButton{\n"
"    border:none;\n"
"}\n"
"#miniSizeButton::pressed{\n"
"    background:#c0d5d6;\n"
"}")
        self.miniSizeButton.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon/miniBar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.miniSizeButton.setIcon(icon13)
        self.miniSizeButton.setIconSize(QtCore.QSize(25, 25))
        self.miniSizeButton.setObjectName("miniSizeButton")
        self.horizontalLayout_4.addWidget(self.miniSizeButton)
        self.verticalLayout_2.addWidget(self.DoingWidget)
        self.verticalLayout_2.setStretch(0, 9)
        self.verticalLayout.addWidget(self.mainWidget)
        self.verticalLayout.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.miniPushButton.clicked.connect(MainWindow.showMinimized)
        self.closePushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.firstPageButton.setText(_translate("MainWindow", "首页       "))
        self.statisButton.setText(_translate("MainWindow", "农场统计"))
        self.taskButton.setText(_translate("MainWindow", "任务展板"))
        self.memoButton.setText(_translate("MainWindow", "日志备忘"))
        self.marketButton.setText(_translate("MainWindow", "番茄市场"))
        self.settingButton.setToolTip(_translate("MainWindow", "设置"))
        self.introButton.setToolTip(_translate("MainWindow", "软件介绍"))
        self.label_2.setText(_translate("MainWindow", "当前番茄任务："))
        self.label_4.setText(_translate("MainWindow", "番茄个数："))
        self.label_6.setText(_translate("MainWindow", "/"))
        self.label_8.setText(_translate("MainWindow", "当前状态："))
        self.redoTimerButton.setToolTip(_translate("MainWindow", "重置番茄钟"))
        self.startTimerButton.setToolTip(_translate("MainWindow", "开始任务番茄钟"))
        self.pauseTimerButton.setToolTip(_translate("MainWindow", "暂停番茄钟"))
        self.stopTimerButton.setToolTip(_translate("MainWindow", "停止番茄钟"))
        self.miniSizeButton.setToolTip(_translate("MainWindow", "迷你计时器"))

from UI.namelabel import nameLabel
import UI.icons_rc
