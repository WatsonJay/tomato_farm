# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'marketItem.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_marketItem(object):
    def setupUi(self, marketItem):
        marketItem.setObjectName("marketItem")
        marketItem.resize(408, 60)
        marketItem.setMinimumSize(QtCore.QSize(408, 60))
        marketItem.setMaximumSize(QtCore.QSize(16777215, 60))
        self.verticalLayout = QtWidgets.QVBoxLayout(marketItem)
        self.verticalLayout.setContentsMargins(7, 4, 7, 4)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(marketItem)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.commNameLabel = QtWidgets.QLabel(marketItem)
        self.commNameLabel.setMinimumSize(QtCore.QSize(130, 0))
        self.commNameLabel.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.commNameLabel.setFont(font)
        self.commNameLabel.setText("")
        self.commNameLabel.setObjectName("commNameLabel")
        self.horizontalLayout.addWidget(self.commNameLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(marketItem)
        self.label_5.setMinimumSize(QtCore.QSize(60, 0))
        self.label_5.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.coinLabel = QtWidgets.QLabel(marketItem)
        self.coinLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.coinLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.coinLabel.setFont(font)
        self.coinLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.coinLabel.setObjectName("coinLabel")
        self.horizontalLayout.addWidget(self.coinLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(marketItem)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.timeLabel = QtWidgets.QLabel(marketItem)
        self.timeLabel.setMinimumSize(QtCore.QSize(160, 0))
        self.timeLabel.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.timeLabel.setFont(font)
        self.timeLabel.setText("")
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout_2.addWidget(self.timeLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.saleLabel = QtWidgets.QLabel(marketItem)
        self.saleLabel.setText("")
        self.saleLabel.setObjectName("saleLabel")
        self.horizontalLayout_2.addWidget(self.saleLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(marketItem)
        QtCore.QMetaObject.connectSlotsByName(marketItem)

    def retranslateUi(self, marketItem):
        _translate = QtCore.QCoreApplication.translate
        marketItem.setWindowTitle(_translate("marketItem", "Form"))
        self.label_2.setText(_translate("marketItem", "商品名称："))
        self.label_5.setText(_translate("marketItem", "番茄币："))
        self.coinLabel.setText(_translate("marketItem", "0"))
        self.label_3.setText(_translate("marketItem", "发布日期："))
