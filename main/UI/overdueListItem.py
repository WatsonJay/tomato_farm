# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'overdueListItem.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_overdueListItem(object):
    def setupUi(self, overdueListItem):
        overdueListItem.setObjectName("overdueListItem")
        overdueListItem.resize(319, 55)
        self.verticalLayout = QtWidgets.QVBoxLayout(overdueListItem)
        self.verticalLayout.setContentsMargins(6, 3, 1, 5)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateLabel = QtWidgets.QLabel(overdueListItem)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.dateLabel.setFont(font)
        self.dateLabel.setText("")
        self.dateLabel.setIndent(-1)
        self.dateLabel.setObjectName("dateLabel")
        self.verticalLayout.addWidget(self.dateLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radiusLabel = QtWidgets.QLabel(overdueListItem)
        self.radiusLabel.setMinimumSize(QtCore.QSize(12, 12))
        self.radiusLabel.setMaximumSize(QtCore.QSize(12, 12))
        self.radiusLabel.setStyleSheet("#radiusLabel{\n"
"    border-radius:6px;\n"
"    background:white;\n"
"}")
        self.radiusLabel.setText("")
        self.radiusLabel.setObjectName("radiusLabel")
        self.horizontalLayout.addWidget(self.radiusLabel)
        self.taskNameLabel = nameLabel(overdueListItem)
        self.taskNameLabel.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.taskNameLabel.setFont(font)
        self.taskNameLabel.setText("")
        self.taskNameLabel.setIndent(-1)
        self.taskNameLabel.setObjectName("taskNameLabel")
        self.horizontalLayout.addWidget(self.taskNameLabel)
        self.buttonWidget = QtWidgets.QWidget(overdueListItem)
        self.buttonWidget.setMaximumSize(QtCore.QSize(70, 16777215))
        self.buttonWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonWidget.setStyleSheet("#buttonWidget>QPushButton{\n"
"    border:none;\n"
"    border-radius:12px;\n"
"}")
        self.buttonWidget.setObjectName("buttonWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.buttonWidget)
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startButton = QtWidgets.QPushButton(self.buttonWidget)
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
        self.horizontalLayout_2.addWidget(self.startButton)
        self.deleteButton = QtWidgets.QPushButton(self.buttonWidget)
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
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.horizontalLayout.addWidget(self.buttonWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(overdueListItem)
        QtCore.QMetaObject.connectSlotsByName(overdueListItem)

    def retranslateUi(self, overdueListItem):
        _translate = QtCore.QCoreApplication.translate
        overdueListItem.setWindowTitle(_translate("overdueListItem", "Form"))

from UI.namelabel import nameLabel
import UI.icons_rc
