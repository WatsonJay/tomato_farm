# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:34
# @Author  : Jaywatson
# @File    : memoWidgetImpl.py
# @Soft    : tomato_farm
import uuid
from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QMenu, QAction

from UI.memoWidget import Ui_memoWidget
from UIImpls.inputImpl import inputDialogImpl
from UIImpls.memoViewImpl import memoViewImpl
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
        self.createBtnMenu()
        self.treeWidget.itemExpanded.connect(self.collapseOther)
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.createRightMenu)
        self.calendarWidget.clicked.connect(self.dayDirCreate)

    # 加载文件树
    def loadTree(self):
        try:
            self.treeWidget.clear()
            self.yearDict.clear()
            sql = 'select * from t_base_node'
            datas = self.sqlite.executeQuery(sql)
            # datas = [
            #     {"id": "1", "node_name": "1", "connect_date":"2020-01-03", "is_folder": 1, "parent_id": "0"},
            #     {"id": "2", "node_name": "2", "connect_date":"2020-01-03", "is_folder": 0, "parent_id": "1"},
            #     {"id": "5", "node_name": "5", "connect_date":"2020-01-03", "is_folder": 1, "parent_id": "1"},
            #     {"id": "6", "node_name": "6", "connect_date":"2020-01-03", "is_folder": 0, "parent_id": "5"},
            #     {"id": "7", "node_name": "7", "connect_date":"2020-01-03", "is_folder": 0, "parent_id": "5"},
            #     {"id": "3", "node_name": "3", "connect_date":"2020-02-03", "is_folder": 1, "parent_id": "0"},
            #     {"id": "4", "node_name": "4", "connect_date":"2019-02-03", "is_folder": 0, "parent_id": "0"}
            # ]
            for data in datas:
                date = datetime.strptime(data['connect_date'], '%Y-%m-%d')
                year = str(date.year)
                month = date.strftime('%m')
                day = date.strftime('%d')
                # 日期节点检查
                dayNode = self.createDateNode(year, month, day)
                if data['parent_id'] != "0":
                    if data['parent_id'] in dayNode.dict.keys():
                        node = self.createNodeByDict(dayNode.dict[data['parent_id']], data)
                    else:
                        return
                else:
                    node = self.createNodeByDict(dayNode, data)
                dayNode.dict[data['id']] = node
            self.tempNodes.clear()
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmemo.error(e)

    # 文件夹检查
    def nodeCheck(self, node, type):
        if "folder" in node.sign and type == "child":
            parent_id = node.id
        elif "folder" in node.sign and type == "same" and "date" not in node.parent().sign:
            parent_id = node.parent().id
        elif "file" not in node.sign and (("unAddAble" not in node.parent().sign and type == "same") or (
                "unaddable" not in node.sign and type == "child")):
            parent_id = "0"
        else:
            parent_id = None
        if hasattr(node, "date"):
            date = node.date
        elif hasattr(node, "data"):
            date = node.data["connect_date"]
        else:
            date = None
        return parent_id,date

    # 添加文件夹
    def createDir(self, node, type):
        try:
            if node != None:
                parent_id,date = self.nodeCheck(node, type)
                if parent_id == None or date == None:
                    self.Tips("该节点无法添加")
                    return
                sql = "Insert Into t_base_node (id,node_name,is_folder,parent_id,connect_date) values (?,?,?,?,?)"
                inputDialog = inputDialogImpl()
                if inputDialog.exec() == inputDialog.Accepted:
                    name = inputDialog.inputLineEdit.text()
                self.sqlite.execute(sql, [str(uuid.uuid1()), name, 1, parent_id, date])
                self.loadTree()
            else:
                self.Tips("未选择节点")
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmemo.error(e)

    # 添加备忘
    def creatememo(self, node, type):
        if node != None:
            parent_id, date = self.nodeCheck(node, type)
            if parent_id == None or date == None:
                self.Tips("该节点无法添加")
                return
            data = {"id": str(uuid.uuid1()), "node_name": "(无标题)", "connect_date": date, "is_folder": 0, "parent_id": parent_id}
            self.createNodeByDict(node, data)
            memoView = memoViewImpl()
            memoView.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.mdiArea.addSubWindow(memoView)
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.Tips("未选择节点")

    # 创建时间节点
    def createDateNode(self, year, month, day):
        if year not in self.yearDict.keys():
            yearNode = self.createNodeByString(self.treeWidget, year, year+"年", ["date", "unAddAble"])
            self.yearDict[year] = yearNode
            self.tempNodes.append(yearNode)
        else:
            yearNode = self.yearDict[year]
        if month not in yearNode.dict.keys():
            monthNode = self.createNodeByString(yearNode, month, month+"月", ["date", "unAddAble"])
            yearNode.dict[month] = monthNode
            self.tempNodes.append(monthNode)
        else:
            monthNode = yearNode.dict[month]
        if day not in monthNode.dict.keys():
            dayNode = self.createNodeByString(monthNode, day, day+"日", ["date"])
            dayNode.date = year + "-" + month + "-" + day
            monthNode.dict[day] = dayNode
            self.tempNodes.append(dayNode)
        else:
            dayNode = monthNode.dict[day]
        return dayNode

    # 字符串创建节点
    def createNodeByString(self, parent, id="", text="", sign=[]):
        node = QTreeWidgetItem(parent)
        icon = self.buildicon("folder")
        node.setIcon(0, icon)
        node.id = id
        node.sign = sign
        node.setText(0, text)
        node.dict = {}
        return node

    # 字典创建节点
    def createNodeByDict(self, parent, data):
        node = QTreeWidgetItem(parent)
        if data['is_folder'] == 0:
            type = "file"
        else:
            type = "folder"
        icon = self.buildicon(type)
        node.data = data
        node.sign = [type]
        node.setIcon(0, icon)
        node.id = data['id']
        node.setText(0, data['node_name'])
        return node

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
            dayNode = self.createDateNode(date[0], date[1], date[2])
            self.treeWidget.setCurrentItem(dayNode)
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmemo.error(e)

    # 图标类型
    def buildicon(self, type):
        icon = QIcon()
        if type == "folder":
            icon.addPixmap(QPixmap(":/icon/folder.png"), QIcon.Normal, QIcon.Off)
        if type == "file":
            icon.addPixmap(QPixmap(":/icon/file.png"), QIcon.Normal, QIcon.Off)
        return icon

    # 手风琴效果
    def collapseOther(self, item):
        currentTop = item
        while currentTop.parent() != None:
            for i in range(currentTop.parent().childCount()):
                if currentTop != currentTop.parent().child(i):
                    self.treeWidget.collapseItem(currentTop.parent().child(i))
            currentTop = currentTop.parent()
        for i in range(self.treeWidget.topLevelItemCount()):
            if currentTop != self.treeWidget.topLevelItem(i):
                self.treeWidget.collapseItem(self.treeWidget.topLevelItem(i))

    # 创建右键菜单
    def createRightMenu(self, pos):
        itemSelect = self.treeWidget.itemAt(pos)
        if itemSelect != None:
            if "unAddAble" not in itemSelect.sign:
                rightMenu = QMenu()
                icon = QIcon()
                icon.addPixmap(QPixmap(":/icon/add_file.png"), QIcon.Normal, QIcon.Off)
                addNodeMemoAction = QAction(icon, '新增子备忘', self)
                addNodeMemoAction.triggered.connect(lambda: self.creatememo(self.treeWidget.currentItem(), "child"))
                icon.addPixmap(QPixmap(":/icon/add_dir.png"), QIcon.Normal, QIcon.Off)
                addNodeDirAction = QAction(icon, '新增子文件夹', self)
                addNodeDirAction.triggered.connect(lambda: self.createDir(self.treeWidget.currentItem(), "child"))
                rightMenu.addAction(addNodeMemoAction)
                rightMenu.addAction(addNodeDirAction)
                if "date" not in itemSelect.sign:
                    if "file" in itemSelect.sign:
                        icon.addPixmap(QPixmap(":/icon/del_file.png"), QIcon.Normal, QIcon.Off)
                        delNodeAction = QAction(icon, '删除备忘', self)
                    if "folder" in itemSelect.sign:
                        icon.addPixmap(QPixmap(":/icon/del_dir.png"), QIcon.Normal, QIcon.Off)
                        delNodeAction = QAction(icon, '删除文件夹', self)
                    icon.addPixmap(QPixmap(":/icon/edit_black.png"), QIcon.Normal, QIcon.Off)
                    editNodeDirAction = QAction(icon, '编辑', self)
                    rightMenu.addAction(editNodeDirAction)
                    rightMenu.addAction(delNodeAction)
                rightMenu.exec_(self.treeWidget.mapToGlobal(pos))
            else:
                return

    # 创建按键菜单
    def createBtnMenu(self):
        btnMenu = QMenu()
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/add_file.png"), QIcon.Normal, QIcon.Off)
        addNodeMemoAction = QAction(icon, '新增子备忘', self)
        addNodeMemoAction.triggered.connect(lambda: self.creatememo(self.treeWidget.currentItem(), "child"))
        icon.addPixmap(QPixmap(":/icon/add_file.png"), QIcon.Normal, QIcon.Off)
        addMemoAction = QAction(icon, '新增平级备忘', self)
        addMemoAction.triggered.connect(lambda: self.creatememo(self.treeWidget.currentItem(), "same"))
        icon.addPixmap(QPixmap(":/icon/add_dir.png"), QIcon.Normal, QIcon.Off)
        addNodeDirAction = QAction(icon, '新增子文件夹', self)
        addNodeDirAction.triggered.connect(lambda : self.createDir(self.treeWidget.currentItem(), "child"))
        icon.addPixmap(QPixmap(":/icon/add_dir.png"), QIcon.Normal, QIcon.Off)
        addDirAction = QAction(icon, '新增平级文件夹', self)
        addDirAction.triggered.connect(lambda: self.createDir(self.treeWidget.currentItem(), "same"))
        btnMenu.addAction(addNodeMemoAction)
        btnMenu.addAction(addMemoAction)
        btnMenu.addSeparator()  # 分割行
        btnMenu.addAction(addNodeDirAction)
        btnMenu.addAction(addDirAction)
        self.showMenuButton.setMenu(btnMenu)