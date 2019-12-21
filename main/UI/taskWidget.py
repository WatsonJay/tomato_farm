# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_taskWidget(object):
    def setupUi(self, taskWidget):
        taskWidget.setObjectName("taskWidget")
        taskWidget.resize(886, 541)
        taskWidget.setWindowTitle("")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(taskWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(taskWidget)
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
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setContentsMargins(0, 1, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(9, 1, 0, 1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addTaskButton = QtWidgets.QPushButton(self.page)
        self.addTaskButton.setMinimumSize(QtCore.QSize(24, 24))
        self.addTaskButton.setMaximumSize(QtCore.QSize(24, 24))
        self.addTaskButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:12px;\n"
"    background:#6CE872;\n"
"}")
        self.addTaskButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTaskButton.setIcon(icon)
        self.addTaskButton.setIconSize(QtCore.QSize(12, 12))
        self.addTaskButton.setObjectName("addTaskButton")
        self.horizontalLayout.addWidget(self.addTaskButton)
        self.modifTaskButton = QtWidgets.QPushButton(self.page)
        self.modifTaskButton.setMinimumSize(QtCore.QSize(24, 24))
        self.modifTaskButton.setMaximumSize(QtCore.QSize(24, 24))
        self.modifTaskButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:12px;\n"
"    background:#FEE66E;\n"
"}")
        self.modifTaskButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modifTaskButton.setIcon(icon1)
        self.modifTaskButton.setIconSize(QtCore.QSize(12, 12))
        self.modifTaskButton.setObjectName("modifTaskButton")
        self.horizontalLayout.addWidget(self.modifTaskButton)
        self.delTaskButton = QtWidgets.QPushButton(self.page)
        self.delTaskButton.setMinimumSize(QtCore.QSize(24, 24))
        self.delTaskButton.setMaximumSize(QtCore.QSize(24, 24))
        self.delTaskButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:12px;\n"
"    background:#F95D5C;\n"
"}")
        self.delTaskButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/delete_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delTaskButton.setIcon(icon2)
        self.delTaskButton.setIconSize(QtCore.QSize(12, 12))
        self.delTaskButton.setObjectName("delTaskButton")
        self.horizontalLayout.addWidget(self.delTaskButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.TaskListWidget = QtWidgets.QListWidget(self.page)
        self.TaskListWidget.setStyleSheet("QListWidget{\n"
"    border:none;\n"
"    background-color: rgba(209, 209, 209, 90);\n"
"}")
        self.TaskListWidget.setObjectName("TaskListWidget")
        self.verticalLayout_4.addWidget(self.TaskListWidget)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.historyListWidget = QtWidgets.QListWidget(self.tab_2)
        self.historyListWidget.setStyleSheet("QListWidget{\n"
"    border:none;\n"
"    background-color: rgba(209, 209, 209, 90);\n"
"}")
        self.historyListWidget.setObjectName("historyListWidget")
        self.verticalLayout_5.addWidget(self.historyListWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.linkDayButton = QtWidgets.QPushButton(taskWidget)
        self.linkDayButton.setMinimumSize(QtCore.QSize(40, 40))
        self.linkDayButton.setMaximumSize(QtCore.QSize(40, 40))
        self.linkDayButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:6px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#c0d5d6;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#c0d5d6;\n"
"}")
        self.linkDayButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.linkDayButton.setIcon(icon3)
        self.linkDayButton.setIconSize(QtCore.QSize(20, 20))
        self.linkDayButton.setObjectName("linkDayButton")
        self.verticalLayout_3.addWidget(self.linkDayButton)
        self.undoLinkButton = QtWidgets.QPushButton(taskWidget)
        self.undoLinkButton.setMinimumSize(QtCore.QSize(40, 40))
        self.undoLinkButton.setMaximumSize(QtCore.QSize(40, 40))
        self.undoLinkButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:6px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#c0d5d6;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#c0d5d6;\n"
"}")
        self.undoLinkButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoLinkButton.setIcon(icon4)
        self.undoLinkButton.setIconSize(QtCore.QSize(20, 20))
        self.undoLinkButton.setObjectName("undoLinkButton")
        self.verticalLayout_3.addWidget(self.undoLinkButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(taskWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.label_2 = QtWidgets.QLabel(taskWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dayTaskListWidget = QtWidgets.QListWidget(taskWidget)
        self.dayTaskListWidget.setStyleSheet("QListWidget{\n"
"    border:none;\n"
"    background-color: rgba(209, 209, 209, 90);\n"
"}")
        self.dayTaskListWidget.setObjectName("dayTaskListWidget")
        self.verticalLayout.addWidget(self.dayTaskListWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(taskWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(taskWidget)

    def retranslateUi(self, taskWidget):
        _translate = QtCore.QCoreApplication.translate
        self.addTaskButton.setToolTip(_translate("taskWidget", "新增"))
        self.modifTaskButton.setToolTip(_translate("taskWidget", "修改"))
        self.delTaskButton.setToolTip(_translate("taskWidget", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("taskWidget", "任务箱"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("taskWidget", "历史任务"))
        self.linkDayButton.setToolTip(_translate("taskWidget", "添加到当日"))
        self.undoLinkButton.setToolTip(_translate("taskWidget", "移除选中任务"))
        self.label_2.setText(_translate("taskWidget", "当日任务"))
import UI.icons_rc
