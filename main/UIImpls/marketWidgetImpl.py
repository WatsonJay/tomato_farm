# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:32
# @Author  : Jaywatson
# @File    : marketWidgetImpl.py
# @Soft    : tomato_farm
import datetime
import uuid

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QMessageBox

from UI.marketWidget import Ui_marketWidget
from UIImpls.marketItemImpl import marketItemImpl
from UIImpls.tipImpl import tipImpl
from util.loadData import sqlite
from util.logger import logger


class marketWidgetImpl(QWidget, Ui_marketWidget, tipImpl):
    # 初始化
    def __init__(self, parent=None):
        super(marketWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        log = logger()
        self.confmarket = log.getlogger('gui')
        self.sqlite = sqlite('./config/tomato.db')
        self.id = ''
        self.deleteWidget.hide()
        self.addButton.clicked.connect(self.addCommodity)
        self.modifButton.clicked.connect(self.modifCommodity)
        self.deleteButton.clicked.connect(self.deleteCommodity)
        self.commitButton.clicked.connect(self.commitCommodity)
        self.cancleButton.clicked.connect(self.cancel)
        self.listWidget.clicked.connect(self.showCommodity)

    # 列出所有任务
    def loadMarket(self):
        self.listWidget.clear()
        try:
            sql = "select * from t_base_commodity ORDER by is_sale ASC"
            datas = self.sqlite.executeQuery(sql)
            for data in datas:
                marketItem, ListItem = self.makeItem(data)
                self.listWidget.addItem(ListItem)
                self.listWidget.setItemWidget(ListItem, marketItem)
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmarket.error(e)

    # 显示商品信息
    def showCommodity(self):
        if len(self.listWidget.selectedItems()) > 0:
            selectedItem = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
            self.id = selectedItem.commodity['id']
            self.commNameLabel.setText(selectedItem.commodity['comm_name'])
            self.commPriceLabel.setText(str(selectedItem.commodity['comm_price']))
            self.createTimeLabel.setText(selectedItem.commodity['create_time'])
            self.buyTimeLabel.setText(selectedItem.commodity['buy_time'])
            self.linkLabel.setText("<a href=%s><b>%s</b></a>" % (selectedItem.commodity['link'],selectedItem.commodity['link']))
            self.descLabel.setText(selectedItem.commodity['comm_desc'])
            buyTime = datetime.datetime.strptime(selectedItem.commodity['buy_time'], "%Y-%m-%d").date()
            now = datetime.date.today()
            if buyTime < now:
                self.deleteWidget.setVisible(True)
            if selectedItem.commodity['is_sale'] == 1:
                self.buyButton.setDisabled(True)
    # 新增商品
    def addCommodity(self):
        self.commNameLineEdit.setText("")
        self.commPriceBox.setValue(0)
        self.buyDateEdit.setDate(QDate.currentDate())
        self.noRadioButton.setChecked(True)
        self.descEdit.setText("")
        self.stackedWidget.setCurrentIndex(1)

    # 编辑商品
    def modifCommodity(self):
        if len(self.listWidget.selectedItems()) > 0:
            selectedItem = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
            if selectedItem.commodity['is_sale'] == 0:
                self.id = selectedItem.commodity['id']
                self.commNameLineEdit.setText(selectedItem.commodity['comm_name'])
                self.commPriceBox.setValue(selectedItem.commodity['comm_price'])
                self.buyDateEdit.setDate(QDate.fromString(selectedItem.commodity['buy_time'], 'yyyy-MM-dd'))
                if selectedItem.commodity['is_alert'] == 1:
                    self.yesRadioButton.setChecked(True)
                else:
                    self.noRadioButton.setChecked(True)
                self.linkLineEdit.setText(selectedItem.commodity['link'])
                self.descEdit.setText(selectedItem.commodity['comm_desc'])
                self.stackedWidget.setCurrentIndex(1)
            else:
                self.Tips("已售商品无法编辑")

    # 删除任务
    def deleteCommodity(self):
        try:
            if len(self.listWidget.selectedItems()) > 0:
                reply = QMessageBox.question(self, '删除确认', '你确定要删除吗?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    selectedItem = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
                    id = selectedItem.commodity['id']
                    sql = "Delete from t_base_commodity where id = ?"
                    self.sqlite.execute(sql, id)
                    self.Tips("已删除任务")
                    self.loadTask()
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmarket.error(e)

    # 提交任务
    def commitCommodity(self):
        try:
            if self.commNameLineEdit.text() != '':
                if self.yesRadioButton.isChecked():
                    isAlert = 1
                else:
                    isAlert = 0
                if self.id == '':
                    sql = "Insert Into t_base_commodity (id,comm_name,comm_price,buy_time,is_alert,link,comm_desc) values (?,?,?,?,?,?,?)"
                    self.sqlite.execute(sql,
                                        [str(uuid.uuid1()), self.commNameLineEdit.text(), self.commPriceBox.value(),
                                         self.buyDateEdit.text(), isAlert, self.linkLineEdit.text(),
                                         self.descEdit.toPlainText()])
                else:
                    sql = "Update t_base_commodity SET comm_name=?,comm_price=?,buy_time=?,is_alert=?,link=?,comm_desc=? where id=?"
                    self.sqlite.execute(sql, [self.commNameLineEdit.text(), self.commPriceBox.value(),
                                              self.buyDateEdit.text(), isAlert, self.linkLineEdit.text(),
                                              self.descEdit.toPlainText(), self.id])
                self.Tips("提交成功")
                self.stackedWidget.setCurrentIndex(0)
                self.loadMarket()
                self.id = ''
            else:
                self.Tips("请填写商品名")
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmarket.error(e)
            self.id = ''

    # 取消
    def cancel(self):
        self.stackedWidget.setCurrentIndex(0)
        self.id = ''

    # 创建列表项
    def makeItem(self, data):
        marketItem = marketItemImpl()
        marketItem.setInfo(data)
        ListItem = QListWidgetItem()
        ListItem.setSizeHint(marketItem.size())
        return marketItem, ListItem
