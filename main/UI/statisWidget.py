# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statisWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statisWidget(object):
    def setupUi(self, statisWidget):
        statisWidget.setObjectName("statisWidget")
        statisWidget.resize(886, 541)
        statisWidget.setWindowTitle("")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(statisWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.todayChartWidget = QtWidgets.QWidget(statisWidget)
        self.todayChartWidget.setObjectName("todayChartWidget")
        self.horizontalLayout.addWidget(self.todayChartWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.todayLabel = QtWidgets.QLabel(statisWidget)
        self.todayLabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.todayLabel.setFont(font)
        self.todayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.todayLabel.setObjectName("todayLabel")
        self.verticalLayout.addWidget(self.todayLabel)
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_10 = QtWidgets.QLabel(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.dayAvgLabel = QtWidgets.QLabel(statisWidget)
        self.dayAvgLabel.setMinimumSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.dayAvgLabel.setFont(font)
        self.dayAvgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dayAvgLabel.setObjectName("dayAvgLabel")
        self.horizontalLayout_4.addWidget(self.dayAvgLabel)
        self.dayLevelLabel = QtWidgets.QLabel(statisWidget)
        self.dayLevelLabel.setMinimumSize(QtCore.QSize(30, 30))
        self.dayLevelLabel.setMaximumSize(QtCore.QSize(30, 30))
        self.dayLevelLabel.setText("")
        self.dayLevelLabel.setObjectName("dayLevelLabel")
        self.horizontalLayout_4.addWidget(self.dayLevelLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem3)
        self.weekLabel = QtWidgets.QLabel(statisWidget)
        self.weekLabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.weekLabel.setFont(font)
        self.weekLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.weekLabel.setObjectName("weekLabel")
        self.verticalLayout_4.addWidget(self.weekLabel)
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
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.label_12 = QtWidgets.QLabel(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.weekAvgLabel = QtWidgets.QLabel(statisWidget)
        self.weekAvgLabel.setMinimumSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.weekAvgLabel.setFont(font)
        self.weekAvgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.weekAvgLabel.setObjectName("weekAvgLabel")
        self.horizontalLayout_6.addWidget(self.weekAvgLabel)
        self.weekLevelLabel = QtWidgets.QLabel(statisWidget)
        self.weekLevelLabel.setMinimumSize(QtCore.QSize(30, 30))
        self.weekLevelLabel.setMaximumSize(QtCore.QSize(30, 30))
        self.weekLevelLabel.setText("")
        self.weekLevelLabel.setObjectName("weekLevelLabel")
        self.horizontalLayout_6.addWidget(self.weekLevelLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem6)
        self.monthLabel = QtWidgets.QLabel(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.monthLabel.setFont(font)
        self.monthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.monthLabel.setObjectName("monthLabel")
        self.verticalLayout_3.addWidget(self.monthLabel)
        self.label_2 = QtWidgets.QLabel(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.label_13 = QtWidgets.QLabel(statisWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.monthAvgLabel = QtWidgets.QLabel(statisWidget)
        self.monthAvgLabel.setMinimumSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.monthAvgLabel.setFont(font)
        self.monthAvgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.monthAvgLabel.setObjectName("monthAvgLabel")
        self.horizontalLayout_8.addWidget(self.monthAvgLabel)
        self.monthLevelLabel = QtWidgets.QLabel(statisWidget)
        self.monthLevelLabel.setMinimumSize(QtCore.QSize(30, 30))
        self.monthLevelLabel.setMaximumSize(QtCore.QSize(30, 30))
        self.monthLevelLabel.setText("")
        self.monthLevelLabel.setObjectName("monthLevelLabel")
        self.horizontalLayout_8.addWidget(self.monthLevelLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem9)
        self.totalLabel = QtWidgets.QLabel(statisWidget)
        self.totalLabel.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.totalLabel.setFont(font)
        self.totalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalLabel.setObjectName("totalLabel")
        self.verticalLayout_2.addWidget(self.totalLabel)
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
        spacerItem10 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 6)
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
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.weekChartWidget = QtWidgets.QWidget(self.tab)
        self.weekChartWidget.setObjectName("weekChartWidget")
        self.horizontalLayout_5.addWidget(self.weekChartWidget)
        self.weekPieWidget = QtWidgets.QWidget(self.tab)
        self.weekPieWidget.setObjectName("weekPieWidget")
        self.horizontalLayout_5.addWidget(self.weekPieWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.yearComboBox = QtWidgets.QComboBox(self.tab_2)
        self.yearComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.yearComboBox.setObjectName("yearComboBox")
        self.horizontalLayout_7.addWidget(self.yearComboBox)
        self.monthComboBox = QtWidgets.QComboBox(self.tab_2)
        self.monthComboBox.setObjectName("monthComboBox")
        self.horizontalLayout_7.addWidget(self.monthComboBox)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.monthChartWidget = QtWidgets.QWidget(self.tab_2)
        self.monthChartWidget.setObjectName("monthChartWidget")
        self.horizontalLayout_9.addWidget(self.monthChartWidget)
        self.monthPieWidget = QtWidgets.QWidget(self.tab_2)
        self.monthPieWidget.setObjectName("monthPieWidget")
        self.horizontalLayout_9.addWidget(self.monthPieWidget)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
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
        self.todayLabel.setText(_translate("statisWidget", "0"))
        self.label_3.setText(_translate("statisWidget", "本日"))
        self.label_10.setText(_translate("statisWidget", "平均："))
        self.dayAvgLabel.setText(_translate("statisWidget", "0"))
        self.weekLabel.setText(_translate("statisWidget", "0"))
        self.label.setText(_translate("statisWidget", "本周"))
        self.label_12.setText(_translate("statisWidget", "平均："))
        self.weekAvgLabel.setText(_translate("statisWidget", "0"))
        self.monthLabel.setText(_translate("statisWidget", "0"))
        self.label_2.setText(_translate("statisWidget", "本月"))
        self.label_13.setText(_translate("statisWidget", "平均："))
        self.monthAvgLabel.setText(_translate("statisWidget", "0"))
        self.totalLabel.setText(_translate("statisWidget", "0"))
        self.label_4.setText(_translate("statisWidget", "总计"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("statisWidget", "本周记录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("statisWidget", "月记录"))
import UI.icons_rc
