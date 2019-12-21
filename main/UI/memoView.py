# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memoView.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_memoView(object):
    def setupUi(self, memoView):
        memoView.setObjectName("memoView")
        memoView.resize(232, 311)
        self.verticalLayout = QtWidgets.QVBoxLayout(memoView)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleWidget = QtWidgets.QWidget(memoView)
        self.titleWidget.setObjectName("titleWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.titleWidget)
        self.verticalLayout_2.setContentsMargins(6, 9, 6, 4)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.titleWidget)
        self.label_2.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateLabel = QtWidgets.QLabel(self.titleWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.horizontalLayout.addWidget(self.dateLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.titleWidget)
        self.label_4.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.titleLabel = QtWidgets.QLabel(self.titleWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout_2.addWidget(self.titleLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.titleWidget)
        self.textBrowser = QtWidgets.QTextBrowser(memoView)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(memoView)
        QtCore.QMetaObject.connectSlotsByName(memoView)

    def retranslateUi(self, memoView):
        _translate = QtCore.QCoreApplication.translate
        memoView.setWindowTitle(_translate("memoView", "Form"))
        self.label_2.setText(_translate("memoView", "日期："))
        self.dateLabel.setText(_translate("memoView", "TextLabel"))
        self.label_4.setText(_translate("memoView", "标题："))
        self.titleLabel.setText(_translate("memoView", "TextLabel"))
