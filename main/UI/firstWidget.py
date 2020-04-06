# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homeWidget(object):
    def setupUi(self, homeWidget):
        homeWidget.setObjectName("homeWidget")
        homeWidget.resize(886, 541)
        homeWidget.setWindowTitle("")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(homeWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(15, 9, 15, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(homeWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.todayListWidget = QtWidgets.QListWidget(homeWidget)
        self.todayListWidget.setStyleSheet("#todayListWidget{\n"
"    border:none;\n"
"    background-color: rgba(209, 209, 209, 90);\n"
"}")
        self.todayListWidget.verticalScrollBar().setStyleSheet("QScrollBar{width:0px;}")
        self.todayListWidget.setObjectName("todayListWidget")
        self.verticalLayout.addWidget(self.todayListWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(15, 9, 15, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(homeWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.overdueListWidget = QtWidgets.QListWidget(homeWidget)
        self.overdueListWidget.setStyleSheet("#overdueListWidget{\n"
"    border:none;\n"
"    background-color: rgba(209, 209, 209, 90);\n"
"}")
        self.overdueListWidget.verticalScrollBar().setStyleSheet("QScrollBar{width:0px;}")
        self.overdueListWidget.setObjectName("overdueListWidget")
        self.verticalLayout_2.addWidget(self.overdueListWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(15, 9, 15, 9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(homeWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.billTextBrowser = QtWidgets.QTextBrowser(homeWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.billTextBrowser.setFont(font)
        self.billTextBrowser.setStyleSheet("QTextBrowser{\n"
"    border:2px solid #adadad;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"    background: rgba(209, 209, 209, 90);\n"
"}")
        self.billTextBrowser.setObjectName("billTextBrowser")
        self.verticalLayout_3.addWidget(self.billTextBrowser)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(homeWidget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.totalTaskLabel = QtWidgets.QLabel(homeWidget)
        self.totalTaskLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.totalTaskLabel.setFont(font)
        self.totalTaskLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalTaskLabel.setObjectName("totalTaskLabel")
        self.verticalLayout_6.addWidget(self.totalTaskLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.label_9 = QtWidgets.QLabel(homeWidget)
        self.label_9.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.completeTaskLabel = QtWidgets.QLabel(homeWidget)
        self.completeTaskLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.completeTaskLabel.setFont(font)
        self.completeTaskLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.completeTaskLabel.setObjectName("completeTaskLabel")
        self.verticalLayout_8.addWidget(self.completeTaskLabel)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.label_12 = QtWidgets.QLabel(homeWidget)
        self.label_12.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.overdueTaskLabel = QtWidgets.QLabel(homeWidget)
        self.overdueTaskLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.overdueTaskLabel.setFont(font)
        self.overdueTaskLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.overdueTaskLabel.setObjectName("overdueTaskLabel")
        self.verticalLayout_7.addWidget(self.overdueTaskLabel)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_7.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem6)
        self.label_13 = QtWidgets.QLabel(homeWidget)
        self.label_13.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.undoTaskLabel = QtWidgets.QLabel(homeWidget)
        self.undoTaskLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.undoTaskLabel.setFont(font)
        self.undoTaskLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.undoTaskLabel.setObjectName("undoTaskLabel")
        self.verticalLayout_9.addWidget(self.undoTaskLabel)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_9.addItem(spacerItem7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.label_6 = QtWidgets.QLabel(homeWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(homeWidget)
        self.label_4.setMinimumSize(QtCore.QSize(80, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.tomatoCoinLabel = QtWidgets.QLabel(homeWidget)
        self.tomatoCoinLabel.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tomatoCoinLabel.setFont(font)
        self.tomatoCoinLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tomatoCoinLabel.setObjectName("tomatoCoinLabel")
        self.horizontalLayout_4.addWidget(self.tomatoCoinLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.setStretch(0, 7)
        self.verticalLayout_4.setStretch(1, 3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.setStretch(0, 6)
        self.verticalLayout_5.setStretch(1, 4)

        self.retranslateUi(homeWidget)
        QtCore.QMetaObject.connectSlotsByName(homeWidget)

    def retranslateUi(self, homeWidget):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("homeWidget", "今日任务"))
        self.label_2.setText(_translate("homeWidget", "逾期任务"))
        self.label_5.setText(_translate("homeWidget", "消费记录"))
        self.billTextBrowser.setHtml(_translate("homeWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.label_7.setText(_translate("homeWidget", "任务总数"))
        self.totalTaskLabel.setText(_translate("homeWidget", "0"))
        self.label_9.setText(_translate("homeWidget", "已完成"))
        self.completeTaskLabel.setText(_translate("homeWidget", "0"))
        self.label_12.setText(_translate("homeWidget", "已逾期"))
        self.overdueTaskLabel.setText(_translate("homeWidget", "0"))
        self.label_13.setText(_translate("homeWidget", "未完成"))
        self.undoTaskLabel.setText(_translate("homeWidget", "0"))
        self.label_6.setText(_translate("homeWidget", "<html><head/><body><p><img src=\":/icon/storage.png\" width=\"30\" height=\"30\"/></p></body></html>"))
        self.label_4.setText(_translate("homeWidget", "番茄币："))
        self.tomatoCoinLabel.setText(_translate("homeWidget", "0"))
import UI.icons_rc
