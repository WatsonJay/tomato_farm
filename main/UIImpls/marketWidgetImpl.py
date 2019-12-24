# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:32
# @Author  : Jaywatson
# @File    : marketWidgetImpl.py
# @Soft    : tomato_farm
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget

from UI.marketWidget import Ui_marketWidget
from UIImpls.tipImpl import tipImpl


class marketWidgetImpl(QWidget, Ui_marketWidget, tipImpl):
    # 初始化
    def __init__(self, parent=None):
        super(marketWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        self.deleteWidget.hide()
        self.addButton.clicked.connect(self.addCommodity)
        self.cancleButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    def addCommodity(self):
        self.commNameLineEdit.setText("")
        self.commPriceBox.setValue(0)
        self.buyDateEdit.setDate(QDate.currentDate())
        self.noRadioButton.setChecked(True)
        self.descEdit.setText("")
        self.stackedWidget.setCurrentIndex(1)