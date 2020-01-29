# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:34
# @Author  : Jaywatson
# @File    : memoWidgetImpl.py
# @Soft    : tomato_farm
from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QMenu, QAction

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
        self.tempNodes = []
        self.yearDict = {}
        self.confmemo = log.getlogger('gui')
        self.sqlite = sqlite('./config/tomato.db')
        self.loadTree()
        self.creatBtnMenu()
        self.treeWidget.itemExpanded.connect(self.collapseOther)
        self.treeWidget.itemChanged.connect(self.editNode)
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.creatRightMenu)
        self.calendarWidget.clicked.connect(self.dayDirCreate)

    # 手风琴效果
    def collapseOther(self,item):
        currentTop = item
        while currentTop.parent() != None:
            for i in range(currentTop.parent().childCount()):
                if currentTop != currentTop.parent().child(i):
                    self.treeWidget.collapseItem(currentTop.parent().child(i))
            currentTop = currentTop.parent()
        for i in range(self.treeWidget.topLevelItemCount()):
            if currentTop != self.treeWidget.topLevelItem(i):
                self.treeWidget.collapseItem(self.treeWidget.topLevelItem(i))

    # 加载文件树
    def loadTree(self):
        try:
            self.treeWidget.clear()
            sql = 'select * from t_base_node'
            datas = self.sqlite.executeQuery(sql)
            # for data in datas:
            #     date = datetime.strptime(data['connect_date'], '%Y-%m-%d')
            #     year = str(date.year)
            #     month = str(date.month)
            #     day = str(date.day)
            self.loadDefaultNode("2020", "01", "03", {"id": "1", "node_name": "1", "is_folder": 1, "parent_id": "0"})
            self.loadDefaultNode("2020", "01", "03", {"id": "2", "node_name": "2", "is_folder": 0, "parent_id": "1"})
            self.loadDefaultNode("2020", "01", "03", {"id": "5", "node_name": "5", "is_folder": 1, "parent_id": "1"})
            self.loadDefaultNode("2020", "01", "03", {"id": "6", "node_name": "6", "is_folder": 0, "parent_id": "5"})
            self.loadDefaultNode("2020", "01", "03", {"id": "7", "node_name": "7", "is_folder": 0, "parent_id": "5"})
            self.loadDefaultNode("2020", "02", "03", {"id": "3", "node_name": "3", "is_folder": 1, "parent_id": "0"})
            self.loadDefaultNode("2019", "02", "03", {"id": "4", "node_name": "4", "is_folder": 0, "parent_id": "0"})
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmemo.error(e)

    # 加载节点
    def loadDefaultNode(self, year, month, day, data):
        dayNode = self.buildDateNode(year, month, day)
        self.tempNodes.clear()
        if data['parent_id'] != "0":
            if data['parent_id'] in dayNode.nodeDict.keys():
                self.loadNode(dayNode, dayNode.nodeDict[data['parent_id']], data)
            else:
                return
        else:
            self.loadNode(dayNode, dayNode, data)

    # 日期节点检查
    def buildDateNode(self, year, month, day):
        if year not in self.yearDict.keys():
            yearNode = QTreeWidgetItem(self.treeWidget)
            icon = self.searchicon(1)
            yearNode.setIcon(0, icon)
            yearNode.id = year
            yearNode.sign = "top"
            yearNode.setText(0, year + "年")
            yearNode.dict = {}
            self.yearDict[year] = yearNode
            self.tempNodes.append(yearNode)
        else:
            yearNode = self.yearDict[year]
        if month not in yearNode.dict.keys():
            monthNode = QTreeWidgetItem(yearNode)
            icon = self.searchicon(1)
            monthNode.setIcon(0, icon)
            monthNode.id = month
            monthNode.sign = "top"
            monthNode.setText(0, month + "月")
            monthNode.dict = {}
            yearNode.dict[month] = monthNode
            self.tempNodes.append(monthNode)
        else:
            monthNode = yearNode.dict[month]
        if day not in monthNode.dict.keys():
            dayNode = QTreeWidgetItem(monthNode)
            icon = self.searchicon(1)
            dayNode.setIcon(0, icon)
            dayNode.id = day
            dayNode.sign = "top"
            dayNode.setText(0, day + "日")
            dayNode.nodeDict = {}
            monthNode.dict[day] = dayNode
            self.tempNodes.append(dayNode)
        else:
            dayNode = monthNode.dict[day]
        return dayNode

    # 加载节点
    def loadNode(self, dayNode, parent, data):
        node = QTreeWidgetItem(parent)
        icon = self.searchicon(data['is_folder'])
        node.setFlags(node.flags() | Qt.ItemIsEditable)
        node.data = data
        node.setIcon(0, icon)
        node.id = data['id']
        if data['is_folder'] == 0:
            node.sign = "file"
        else:
            node.sign = "folder"
        node.setText(0, data['node_name'])
        node.nodeDict = {}
        dayNode.nodeDict[data['id']] = node

    # 图标类型
    def searchicon(self, type):
        icon = QIcon()
        if type == 1:
            icon.addPixmap(QPixmap(":/icon/folder.png"), QIcon.Normal, QIcon.Off)
        else:
            icon.addPixmap(QPixmap(":/icon/file.png"), QIcon.Normal, QIcon.Off)
        return icon

    # 临时节点清理
    def clearTempNode(self):
        while len(self.tempNodes) > 0:
            node = self.tempNodes[-1]
            if node.parent() == None:
                rootIndex = self.treeWidget.indexOfTopLevelItem(node)
                self.yearDict.pop(node.id)
                self.treeWidget.takeTopLevelItem(rootIndex)
            else:
                parent = node.parent()
                parent.dict.pop(node.id)
                parent.removeChild(node)
            self.tempNodes.pop()

    # 日期自动创建文件夹
    def dayDirCreate(self):
        try:
            self.clearTempNode()
            date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd").split("-")
            dayNode = self.buildDateNode(date[0], date[1], date[2])
            self.treeWidget.setCurrentItem(dayNode)
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmemo.error(e)

    # 创建备忘

    # 创建今日备忘

    # 创建文件夹

    # 删除文件夹

    # 编辑节点
    def editNode(self,item):
        print(item.text())

    # 创建右键菜单
    def creatRightMenu(self, pos):
        itemSelect = self.treeWidget.itemAt(pos)
        if itemSelect.sign != "top":
            rightMenu = QMenu()
            icon = QIcon()
            icon.addPixmap(QPixmap(":/icon/add_file.png"), QIcon.Normal, QIcon.Off)
            addNodeMemoAction = QAction(icon, '新增子备忘', self)
            rightMenu.addAction(addNodeMemoAction)
            rightMenu.exec_(self.treeWidget.mapToGlobal(pos))
        else:
            return

    # 创建按键菜单
    def creatBtnMenu(self):
        btnMenu = QMenu()
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/add_file.png"), QIcon.Normal, QIcon.Off)
        addNodeMemoAction = QAction(icon, '新增子备忘', self)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/add_file.png"), QIcon.Normal, QIcon.Off)
        addMemoAction = QAction(icon, '新增平级备忘', self)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/add_dir.png"), QIcon.Normal, QIcon.Off)
        addNodeDirAction = QAction(icon, '新增子文件夹', self)
        btnMenu.addAction(addNodeMemoAction)
        btnMenu.addAction(addMemoAction)
        btnMenu.addSeparator()  # 分割行
        btnMenu.addAction(addNodeDirAction)
        self.showMenuButton.setMenu(btnMenu)
