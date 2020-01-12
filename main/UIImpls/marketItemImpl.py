# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 17:33
# @Author  : Jaywatson
# @File    : marketItemImpl.py
# @Soft    : tomato_farm

from PyQt5.QtWidgets import QWidget

from UI.marketItem import Ui_marketItem


class marketItemImpl(QWidget, Ui_marketItem):

    # 初始化
    def __init__(self, parent=None):
        super(marketItemImpl, self).__init__(parent)
        self.setupUi(self)
        self.commodity = {}

    # 信息填充
    def setInfo(self, data):
        self.commodity = data
        self.commNameLabel.setText(data['comm_name'])
        self.timeLabel.setText(data['create_time'])
        if data['is_sale'] == 1:
            self.saleLabel.setText("<font color=%s>%s</font>" % ('#F95D5C', "已售出"))