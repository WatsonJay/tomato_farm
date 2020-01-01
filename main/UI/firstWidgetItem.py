
# Form implementation generated from reading ui file 'firstWidgetItem.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_firstWidgetItem(object):
    def setupUi(self, firstWidgetItem):
        firstWidgetItem.setObjectName("firstWidgetItem")
        firstWidgetItem.resize(381, 50)
        firstWidgetItem.setMinimumSize(QtCore.QSize(381, 50))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(firstWidgetItem)
        self.horizontalLayout_2.setContentsMargins(-1, 3, -1, 3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(firstWidgetItem)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.taskNameLabel = QtWidgets.QLabel(firstWidgetItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.taskNameLabel.setFont(font)
        self.taskNameLabel.setText("")
        self.taskNameLabel.setObjectName("taskNameLabel")
        self.horizontalLayout.addWidget(self.taskNameLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(firstWidgetItem)
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.duringLabel = QtWidgets.QLabel(firstWidgetItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.duringLabel.setFont(font)
        self.duringLabel.setText("")
        self.duringLabel.setObjectName("duringLabel")
        self.horizontalLayout_4.addWidget(self.duringLabel)
        self.label_3 = QtWidgets.QLabel(firstWidgetItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.widget = QtWidgets.QWidget(firstWidgetItem)
        self.widget.setMinimumSize(QtCore.QSize(66, 0))
        self.widget.setMaximumSize(QtCore.QSize(66, 16777215))
        self.widget.setStyleSheet("QWidget>QPushButton{\n"
"    border:none;\n"
"    border-radius:12px;\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startButton = QtWidgets.QPushButton(self.widget)
        self.startButton.setMinimumSize(QtCore.QSize(24, 24))
        self.startButton.setMaximumSize(QtCore.QSize(24, 24))
        self.startButton.setStyleSheet("#startButton{\n"
"    background:#6CE872;\n"
"}\n"
"\n"
"#startButton::pressed{\n"
"    background:#3c823f;\n"
"}\n"
"")
        self.startButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QtCore.QSize(12, 12))
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_3.addWidget(self.startButton)
        self.deleteButton = QtWidgets.QPushButton(self.widget)
        self.deleteButton.setMinimumSize(QtCore.QSize(24, 24))
        self.deleteButton.setMaximumSize(QtCore.QSize(24, 24))
        self.deleteButton.setStyleSheet("#deleteButton{\n"
"    background:#F95D5C;\n"
"}\n"
"\n"
"#deleteButton::pressed{\n"
"    background:#aa3e3e;\n"
"}")
        self.deleteButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/delete_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setIconSize(QtCore.QSize(12, 12))
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_3.addWidget(self.deleteButton)
        self.doingLabel = QtWidgets.QLabel(self.widget)
        self.doingLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.doingLabel.setFont(font)
        self.doingLabel.setStyleSheet("border:1px soild white;\n"
"border-radius:5px;\n"
"background:#6CE872;\n"
"color:white;")
        self.doingLabel.setText("")
        self.doingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.doingLabel.setObjectName("doingLabel")
        self.horizontalLayout_3.addWidget(self.doingLabel)
        self.horizontalLayout_2.addWidget(self.widget)
        self.horizontalLayout_2.setStretch(0, 9)
        self.horizontalLayout_2.setStretch(1, 1)

        self.retranslateUi(firstWidgetItem)
        QtCore.QMetaObject.connectSlotsByName(firstWidgetItem)

    def retranslateUi(self, firstWidgetItem):
        _translate = QtCore.QCoreApplication.translate
        firstWidgetItem.setWindowTitle(_translate("firstWidgetItem", "Form"))
        self.label.setText(_translate("firstWidgetItem", "任务名："))
        self.label_2.setText(_translate("firstWidgetItem", "任务时长："))
        self.label_3.setText(_translate("firstWidgetItem", "分钟"))
import UI.icons_rc
