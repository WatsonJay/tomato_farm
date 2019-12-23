# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
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
"}\n"
"QPushButton:hover{\n"
"    background:#53b357;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#53b357;\n"
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
"}\n"
"QPushButton:hover{\n"
"    background:#c5b355;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#c5b355;\n"
"}\n"
"")
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
"}\n"
"QPushButton:hover{\n"
"    background:#aa3e3e;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#aa3e3e;\n"
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
        self.taskListWidget = QtWidgets.QListWidget(self.page)
        self.taskListWidget.setStyleSheet("QListWidget{\n"
"    border:none;\n"
"    background-color: rgba(209, 209, 209, 90);\n"
"}")
        self.taskListWidget.setObjectName("taskListWidget")
        self.verticalLayout_4.addWidget(self.taskListWidget)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("QWidget>QLineEdit{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"QWidget>QTextEdit{\n"
"    border:1px solid gray;\n"
"    background:white;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"QWidget>QDateEdit{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"QWidget>QDateEdit::drop-down{\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-left-color: gray; \n"
"}\n"
"QWidget>QDateEdit::down-arrow{\n"
"    border-image:url(:/icon/down.png);\n"
"}\n"
"QWidget>QPushButton{\n"
"    border:none;\n"
"    color:white;\n"
"    border-radius:12px;\n"
"}\n"
"QSpinBox,QDoubleSpinBox{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"/*spinbox 抬起样式*/\n"
"QDoubleSpinBox::up-button,QSpinBox::up-button {\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"    image: url(:/icon/add.png);\n"
"    width: 16px;\n"
"    height: 20px;       \n"
"}\n"
"QDoubleSpinBox::down-button,QSpinBox::down-button {\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"    border-image: url(:/icon/remove.png);\n"
"    width: 16px;\n"
"    height: 17px;\n"
"}\n"
"/*按钮按下样式*/\n"
"QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"    image: url(:/icon/add.png);\n"
"    width: 16px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"    image: url(:/icon/remove.png);\n"
"    width: 16px;\n"
"    height: 17px;\n"
"}")
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.taskNameEdit = QtWidgets.QLineEdit(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.taskNameEdit.setFont(font)
        self.taskNameEdit.setObjectName("taskNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.taskNameEdit)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.taskHourBox = QtWidgets.QSpinBox(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.taskHourBox.setFont(font)
        self.taskHourBox.setMaximum(72)
        self.taskHourBox.setObjectName("taskHourBox")
        self.horizontalLayout_4.addWidget(self.taskHourBox)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.taskMinuteBox = QtWidgets.QSpinBox(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.taskMinuteBox.setFont(font)
        self.taskMinuteBox.setMinimum(1)
        self.taskMinuteBox.setMaximum(60)
        self.taskMinuteBox.setObjectName("taskMinuteBox")
        self.horizontalLayout_4.addWidget(self.taskMinuteBox)
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.taskDeadLineEdit = QtWidgets.QDateEdit(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.taskDeadLineEdit.setFont(font)
        self.taskDeadLineEdit.setCalendarPopup(True)
        self.taskDeadLineEdit.setObjectName("taskDeadLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.taskDeadLineEdit)
        self.label_7 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.taskDescEdit = QtWidgets.QTextEdit(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.taskDescEdit.setFont(font)
        self.taskDescEdit.setObjectName("taskDescEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.taskDescEdit)
        self.verticalLayout_7.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 198, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.commitButton = QtWidgets.QPushButton(self.page_2)
        self.commitButton.setMinimumSize(QtCore.QSize(70, 24))
        self.commitButton.setMaximumSize(QtCore.QSize(70, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.commitButton.setFont(font)
        self.commitButton.setStyleSheet("QPushButton{\n"
"    background:#6CE872;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#53b357;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#53b357;\n"
"}")
        self.commitButton.setObjectName("commitButton")
        self.horizontalLayout_3.addWidget(self.commitButton)
        self.cancleButton = QtWidgets.QPushButton(self.page_2)
        self.cancleButton.setMinimumSize(QtCore.QSize(70, 24))
        self.cancleButton.setMaximumSize(QtCore.QSize(70, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.cancleButton.setFont(font)
        self.cancleButton.setStyleSheet("QPushButton{\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#aa3e3e;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#aa3e3e;\n"
"}")
        self.cancleButton.setObjectName("cancleButton")
        self.horizontalLayout_3.addWidget(self.cancleButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
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
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
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
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(taskWidget)

    def retranslateUi(self, taskWidget):
        _translate = QtCore.QCoreApplication.translate
        self.addTaskButton.setToolTip(_translate("taskWidget", "新增"))
        self.modifTaskButton.setToolTip(_translate("taskWidget", "修改"))
        self.delTaskButton.setToolTip(_translate("taskWidget", "删除"))
        self.label.setText(_translate("taskWidget", "任务名称："))
        self.label_3.setText(_translate("taskWidget", "任务时长："))
        self.label_9.setText(_translate("taskWidget", "小时"))
        self.label_8.setText(_translate("taskWidget", "分钟"))
        self.label_4.setText(_translate("taskWidget", "结束期限："))
        self.taskDeadLineEdit.setDisplayFormat(_translate("taskWidget", "yyyy-M-d"))
        self.label_7.setText(_translate("taskWidget", "任务描述"))
        self.commitButton.setText(_translate("taskWidget", "发布"))
        self.cancleButton.setText(_translate("taskWidget", "取消"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("taskWidget", "任务箱"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("taskWidget", "历史任务"))
        self.linkDayButton.setToolTip(_translate("taskWidget", "添加到当日"))
        self.undoLinkButton.setToolTip(_translate("taskWidget", "移除选中任务"))
        self.label_2.setText(_translate("taskWidget", "当日任务"))

import icons_rc
