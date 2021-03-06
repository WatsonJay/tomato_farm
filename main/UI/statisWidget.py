# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statisWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from UI.barChartView import barChartView
from UI.perBarChartView import perBarChartView
from UI.pieChartView import pieChartView


class Ui_statisWidget(object):
    def setupUi(self, statisWidget):
        statisWidget.setObjectName("statisWidget")
        statisWidget.resize(886, 541)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        statisWidget.setFont(font)
        statisWidget.setWindowTitle("")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(statisWidget)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        #插入图表
        yearXAxis = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
        self.yearTotalView = perBarChartView(yearXAxis)
        self.verticalLayout_8.addWidget(self.yearTotalView)
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.todayLabel = QtWidgets.QLabel(statisWidget)
        self.todayLabel.setMinimumSize(QtCore.QSize(30, 0))
        self.todayLabel.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.todayLabel.setFont(font)
        self.todayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.todayLabel.setObjectName("todayLabel")
        self.horizontalLayout_10.addWidget(self.todayLabel)
        self.dayLevelLabel = QtWidgets.QLabel(statisWidget)
        self.dayLevelLabel.setMinimumSize(QtCore.QSize(30, 30))
        self.dayLevelLabel.setMaximumSize(QtCore.QSize(30, 30))
        self.dayLevelLabel.setText("")
        self.dayLevelLabel.setObjectName("dayLevelLabel")
        self.horizontalLayout_10.addWidget(self.dayLevelLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.lastDayLabel = QtWidgets.QLabel(statisWidget)
        self.lastDayLabel.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.lastDayLabel.setFont(font)
        self.lastDayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lastDayLabel.setObjectName("lastDayLabel")
        self.horizontalLayout_4.addWidget(self.lastDayLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.weekLabel = QtWidgets.QLabel(statisWidget)
        self.weekLabel.setMinimumSize(QtCore.QSize(30, 0))
        self.weekLabel.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.weekLabel.setFont(font)
        self.weekLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.weekLabel.setObjectName("weekLabel")
        self.horizontalLayout_11.addWidget(self.weekLabel)
        self.weekLevelLabel = QtWidgets.QLabel(statisWidget)
        self.weekLevelLabel.setMinimumSize(QtCore.QSize(30, 30))
        self.weekLevelLabel.setMaximumSize(QtCore.QSize(30, 30))
        self.weekLevelLabel.setText("")
        self.weekLevelLabel.setObjectName("weekLevelLabel")
        self.horizontalLayout_11.addWidget(self.weekLevelLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.lastWeekLabel = QtWidgets.QLabel(statisWidget)
        self.lastWeekLabel.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.lastWeekLabel.setFont(font)
        self.lastWeekLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lastWeekLabel.setObjectName("lastWeekLabel")
        self.horizontalLayout_6.addWidget(self.lastWeekLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem6)
        self.label_2 = QtWidgets.QLabel(statisWidget)
        self.label_2.setMinimumSize(QtCore.QSize(90, 0))
        self.label_2.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.monthLabel = QtWidgets.QLabel(statisWidget)
        self.monthLabel.setMinimumSize(QtCore.QSize(30, 0))
        self.monthLabel.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.monthLabel.setFont(font)
        self.monthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.monthLabel.setObjectName("monthLabel")
        self.horizontalLayout_12.addWidget(self.monthLabel)
        self.monthLevelLabel = QtWidgets.QLabel(statisWidget)
        self.monthLevelLabel.setMinimumSize(QtCore.QSize(30, 30))
        self.monthLevelLabel.setMaximumSize(QtCore.QSize(30, 30))
        self.monthLevelLabel.setText("")
        self.monthLevelLabel.setObjectName("monthLevelLabel")
        self.horizontalLayout_12.addWidget(self.monthLevelLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(statisWidget)
        self.label_13.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.lastMonthLabel = QtWidgets.QLabel(statisWidget)
        self.lastMonthLabel.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.lastMonthLabel.setFont(font)
        self.lastMonthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lastMonthLabel.setObjectName("lastMonthLabel")
        self.horizontalLayout_8.addWidget(self.lastMonthLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem9)
        self.label_4 = QtWidgets.QLabel(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.totalLabel = QtWidgets.QLabel(statisWidget)
        self.totalLabel.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.totalLabel.setFont(font)
        self.totalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalLabel.setObjectName("totalLabel")
        self.verticalLayout_2.addWidget(self.totalLabel)
        spacerItem10 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(statisWidget)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"    border: none;\n"
"}\n"
"QTabBar::tab {\n"
"    border: none;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    color: white;\n"
"    border: 1px solid #656565;\n"
"    background:#656565;\n"
"    height: 18px;\n"
"    min-width: 65px;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"}\n"
"QTabBar::tab:hover {\n"
"    color: #656565;\n"
"    background: #E9EAED;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    color: #656565;\n"
"    height: 25px;\n"
"    background: #E9EAED;\n"
"    border-bottom: 1px solid #E9EAED;\n"
"}\n"
"QTabBar::tab:!selected{\n"
"    margin-top:5px;\n"
"}\n"
"\n"
"QTabWidget::pane{\n"
"    border-top: 1px solid #656565;\n"
"    margin-top: -2px;\n"
"}\n"
"#tab,#tab_2,#tab_3,#tab_4{\n"
"    background:#E9EAED;\n"
"}\n"
"QPushButton{\n"
"    border-radius:12px;\n"
"    border:none;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, 4, -1)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.weekRefreshButton = QtWidgets.QPushButton(self.tab)
        self.weekRefreshButton.setMinimumSize(QtCore.QSize(24, 24))
        self.weekRefreshButton.setMaximumSize(QtCore.QSize(24, 24))
        self.weekRefreshButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weekRefreshButton.setIcon(icon)
        self.weekRefreshButton.setIconSize(QtCore.QSize(12, 12))
        self.weekRefreshButton.setObjectName("weekRefreshButton")
        self.horizontalLayout_5.addWidget(self.weekRefreshButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.weekChartLayout = QtWidgets.QVBoxLayout()
        self.weekChartLayout.setObjectName("weekChartLayout")
        # 插入图表
        weekXAxis = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        self.weekChartView = barChartView(weekXAxis)
        self.weekChartView._axis_x.setLabelsAngle(280)
        self.weekChartLayout.addWidget(self.weekChartView)
        self.horizontalLayout_13.addLayout(self.weekChartLayout)
        spacerItem12 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_13.addItem(spacerItem12)
        self.weekPieLayout = QtWidgets.QVBoxLayout()
        self.weekPieLayout.setObjectName("weekPieLayout")
        self.weekPieView = pieChartView()
        self.weekPieLayout.addWidget(self.weekPieView)
        self.horizontalLayout_13.addLayout(self.weekPieLayout)
        self.horizontalLayout_13.setStretch(0, 9)
        self.horizontalLayout_13.setStretch(2, 6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.verticalLayout_7.setStretch(1, 9)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("QPushButton{\n"
"    border-radius:12px;\n"
"    border:none;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}\n"
"QComboBox{\n"
"    border:1px solid gray;\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"QComboBox::drop-down{\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-left-color: gray; \n"
"}\n"
"QComboBox::down-arrow{\n"
"    border-image:url(:/icon/down.png);\n"
"}")
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, -1, 4, -1)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.yearComboBox = QtWidgets.QComboBox(self.tab_2)
        self.yearComboBox.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.yearComboBox.setFont(font)
        self.yearComboBox.setObjectName("yearComboBox")
        self.horizontalLayout_7.addWidget(self.yearComboBox)
        self.monthComboBox = QtWidgets.QComboBox(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.monthComboBox.setFont(font)
        self.monthComboBox.setObjectName("monthComboBox")
        self.horizontalLayout_7.addWidget(self.monthComboBox)
        self.searchButton = QtWidgets.QPushButton(self.tab_2)
        self.searchButton.setMinimumSize(QtCore.QSize(60, 24))
        self.searchButton.setMaximumSize(QtCore.QSize(60, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("color:white")
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_7.addWidget(self.searchButton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.monthRefreshButton = QtWidgets.QPushButton(self.tab_2)
        self.monthRefreshButton.setMinimumSize(QtCore.QSize(24, 24))
        self.monthRefreshButton.setMaximumSize(QtCore.QSize(24, 24))
        self.monthRefreshButton.setText("")
        self.monthRefreshButton.setIcon(icon)
        self.monthRefreshButton.setIconSize(QtCore.QSize(12, 12))
        self.monthRefreshButton.setObjectName("monthRefreshButton")
        self.horizontalLayout_7.addWidget(self.monthRefreshButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.monthChartLayout = QtWidgets.QVBoxLayout()
        self.monthChartLayout.setSpacing(0)
        self.monthChartLayout.setObjectName("monthChartLayout")
        # 插入图表
        self.monthChartView = barChartView()
        self.monthChartView._axis_x.setLabelsAngle(0)
        self.monthChartLayout.addWidget(self.monthChartView)
        self.verticalLayout_6.addLayout(self.monthChartLayout)
        self.verticalLayout_6.setStretch(1, 9)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.setStretch(0, 4)
        self.verticalLayout_5.setStretch(1, 6)

        self.retranslateUi(statisWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(statisWidget)

    def retranslateUi(self, statisWidget):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("statisWidget", "本年度统计"))
        self.label_3.setText(_translate("statisWidget", "本日"))
        self.todayLabel.setText(_translate("statisWidget", "0"))
        self.label_10.setText(_translate("statisWidget", "昨日："))
        self.lastDayLabel.setText(_translate("statisWidget", "0"))
        self.label.setText(_translate("statisWidget", "本周"))
        self.weekLabel.setText(_translate("statisWidget", "0"))
        self.label_12.setText(_translate("statisWidget", "上周："))
        self.lastWeekLabel.setText(_translate("statisWidget", "0"))
        self.label_2.setText(_translate("statisWidget", "本月"))
        self.monthLabel.setText(_translate("statisWidget", "0"))
        self.label_13.setText(_translate("statisWidget", "上月："))
        self.lastMonthLabel.setText(_translate("statisWidget", "0"))
        self.label_4.setText(_translate("statisWidget", "总计"))
        self.totalLabel.setText(_translate("statisWidget", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("statisWidget", "本周记录"))
        self.searchButton.setText(_translate("statisWidget", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("statisWidget", "月记录"))
import UI.icons_rc
