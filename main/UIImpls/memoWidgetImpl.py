# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:34
# @Author  : Jaywatson
# @File    : memoWidgetImpl.py
# @Soft    : tomato_farm
from datetime import datetime

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem

from UI.memoWidget import Ui_memoWidget
from UIImpls.tipImpl import tipImpl
from util.loadData import sqlite
from util.logger import logger


class memoWidgetImpl(QWidget, Ui_memoWidget, tipImpl):
    # 初始化
    def __init__(self, parent=None):
        super(memoWidgetImpl, self).__init__(parent)
        self.setupUi(self)
        log = logger()
        self.yearDict = {}
        self.confmemo = log.getlogger('gui')
        self.sqlite = sqlite('./config/tomato.db')
        self.loadTree()

    #加载文件树
    def loadTree(self):
        try:
            self.treeWidget.clear()
            sql = 'select * from t_base_node'
            datas = self.sqlite.executeQuery(sql)
            # for data in datas:
            #     date = datetime.strptime(data['create_time'], '%Y-%m-%d %H:%M:%S')
            #     year = str(date.year)
            #     month = str(date.month)
            #     day = str(date.day)
            self.createNode("2020", "01", "03", {"id": "", "memo_temp": "", "": ""})
            self.createNode("2020", "02", "03", {"id": "", "memo_temp": "", "": ""})
            self.createNode("2019", "02", "03", {"id": "", "memo_temp": "", "": ""})
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmemo.error(e)

    #创建节点
    def createNode(self,year,month,day,data):
        if year not in self.yearDict.keys():
            yearNode = QTreeWidgetItem(self.treeWidget)
            icon = self.searchicon("folder")
            yearNode.setIcon(0, icon)
            yearNode.setText(0, year + "年")
            yearNode.monthDict = {}
            self.yearDict[year] = yearNode
        else:
            yearNode = self.yearDict[year]
        if month not in yearNode.monthDict.keys():
            monthNode = QTreeWidgetItem(yearNode)
            icon = self.searchicon("folder")
            monthNode.setIcon(0, icon)
            monthNode.setText(0, month + "月")
            monthNode.dayDict = {}
            yearNode.monthDict[month] = monthNode
        else:
            monthNode = yearNode.monthDict[month]
        if day not in monthNode.dayDict.keys():
            dayNode = QTreeWidgetItem(monthNode)
            icon = self.searchicon("folder")
            dayNode.setIcon(0, icon)
            dayNode.setText(0, month + "日")
            dayNode.nodeDict = {}
            monthNode.dayDict[day] = dayNode
        else:
            dayNode = monthNode.dayDict[day]

    #图标类型
    def searchicon(self, type):
        icon = QIcon()
        if type == "folder":
            icon.addPixmap(QPixmap(":/icon/folder.png"), QIcon.Normal, QIcon.Off)
        else:
            icon.addPixmap(QPixmap(":/icon/file.png"), QIcon.Normal, QIcon.Off)
        return icon

