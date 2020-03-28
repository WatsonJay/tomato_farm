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
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QMenu, QAction, QTableWidgetItem, QColorDialog

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
        self.tempNodes = [] #日历创建临时节点存储
        self.yearDict = {} #年节点存储
        self.confmemo = log.getlogger('gui')
        self.sqlite = sqlite('./config/tomato.db')
        self.loadTree()
        self.createBtnMenu()
        # 日历功能
        self.calendarWidget.clicked.connect(self.dayDirCreate)
        # 文件树功能
        self.treeWidget.itemExpanded.connect(self.collapseOther)
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.createRightMenu)
        self.treeWidget.itemDoubleClicked.connect(self.changeShow)
        # 文件列表功能
        self.fileTableWidget.setColumnHidden(0, True)
        self.fileTableWidget.doubleClicked.connect(self.tableOpenMemo)
        # 文件编辑功能
        self.fontColorButton.clicked.connect(self.fileColorBox)

    # 加载文件树
    def loadTree(self):
        try:
            self.treeWidget.clear()
            self.yearDict.clear()
            sql = 'select * from t_base_node order by parent_id ASC'
            datas = self.sqlite.executeQuery(sql)
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

    # 创建时间节点
    def createDateNode(self, year, month, day):
        if year not in self.yearDict.keys():
            yearNode = self.createNodeByString(self.treeWidget, year, year + "年", ["date", "unAddable"])
            self.yearDict[year] = yearNode
            self.tempNodes.append(yearNode)
        else:
            yearNode = self.yearDict[year]
        if month not in yearNode.dict.keys():
            monthNode = self.createNodeByString(yearNode, month, month + "月", ["date", "unAddable"])
            yearNode.dict[month] = monthNode
            self.tempNodes.append(monthNode)
        else:
            monthNode = yearNode.dict[month]
        if day not in monthNode.dict.keys():
            dayNode = self.createNodeByString(monthNode, day, day + "日", ["date"])
            dayNode.date = year + "-" + month + "-" + day
            monthNode.dict[day] = dayNode
            self.tempNodes.append(dayNode)
        else:
            dayNode = monthNode.dict[day]
        return dayNode

    # 字典创建节点
    def createNodeByDict(self, parent, data):
        node = QTreeWidgetItem(parent)
        if data['is_folder'] == 0:
            type = "file"
        else:
            type = "folder"
        icon = self.buildicon(type)
        node.nodeData = data
        node.sign = [type]
        node.setIcon(0, icon)
        node.id = data['id']
        node.setText(0, data['node_name'])
        return node

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
        addNodeDirAction.triggered.connect(lambda: self.createDir(self.treeWidget.currentItem(), "child"))
        icon.addPixmap(QPixmap(":/icon/add_dir.png"), QIcon.Normal, QIcon.Off)
        addDirAction = QAction(icon, '新增平级文件夹', self)
        addDirAction.triggered.connect(lambda: self.createDir(self.treeWidget.currentItem(), "same"))
        btnMenu.addAction(addNodeMemoAction)
        btnMenu.addAction(addMemoAction)
        btnMenu.addSeparator()  # 分割行
        btnMenu.addAction(addNodeDirAction)
        btnMenu.addAction(addDirAction)
        self.showMenuButton.setMenu(btnMenu)

    # 创建右键菜单
    def createRightMenu(self, pos):
        itemSelect = self.treeWidget.itemAt(pos)
        if itemSelect != None:
            if "unAddable" not in itemSelect.sign:
                rightMenu = QMenu()
                icon = QIcon()
                if "file" in itemSelect.sign:
                    icon.addPixmap(QPixmap(":/icon/del_file.png"), QIcon.Normal, QIcon.Off)
                    delNodeAction = QAction(icon, '删除备忘', self)
                    rightMenu.addAction(delNodeAction)
                else:
                    icon.addPixmap(QPixmap(":/icon/add_file.png"), QIcon.Normal, QIcon.Off)
                    addNodeMemoAction = QAction(icon, '新增子备忘', self)
                    addNodeMemoAction.triggered.connect(lambda: self.creatememo(self.treeWidget.currentItem(), "child"))
                    icon.addPixmap(QPixmap(":/icon/add_dir.png"), QIcon.Normal, QIcon.Off)
                    addNodeDirAction = QAction(icon, '新增子文件夹', self)
                    addNodeDirAction.triggered.connect(lambda: self.createDir(self.treeWidget.currentItem(), "child"))
                    rightMenu.addAction(addNodeMemoAction)
                    rightMenu.addAction(addNodeDirAction)
                    if "date" not in itemSelect.sign:
                        if "folder" in itemSelect.sign:
                            icon.addPixmap(QPixmap(":/icon/del_dir.png"), QIcon.Normal, QIcon.Off)
                            delNodeAction = QAction(icon, '删除文件夹', self)
                            delNodeAction.triggered.connect(
                                lambda: self.deleteNode(self.treeWidget.currentItem()))
                            icon.addPixmap(QPixmap(":/icon/edit_black.png"), QIcon.Normal, QIcon.Off)
                            editNodeDirAction = QAction(icon, '编辑', self)
                            editNodeDirAction.triggered.connect(
                                lambda: self.editDir(self.treeWidget.currentItem()))
                            rightMenu.addAction(editNodeDirAction)
                            rightMenu.addAction(delNodeAction)
                rightMenu.exec_(self.treeWidget.mapToGlobal(pos))

    # 添加文件夹
    def createDir(self, node, type):
        try:
            if node != None:
                parent_id, date = self.nodeInfo(node, type)
                if parent_id == "" or date == "":
                    self.Tips("该节点无法添加")
                    return
                sql = "Insert Into t_base_node (id,node_name,is_folder,parent_id,connect_date) values (?,?,?,?,?)"
                inputDialog = inputDialogImpl()
                if inputDialog.exec() == inputDialog.Accepted:
                    name = inputDialog.inputLineEdit.text()
                    self.sqlite.execute(sql, [str(uuid.uuid1()), name, 1, parent_id, date])
                    data = {"id": str(uuid.uuid1()), "node_name": name, "connect_date": date, "is_folder": 1,
                        "parent_id": parent_id, "memo_id": ""}
                    if type == "same":
                        self.createNodeByDict(node.parent(), data)
                    if type == "child":
                        self.createNodeByDict(node, data)
            else:
                self.Tips("未选择节点")
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmemo.error(e)

    # 添加备忘
    def creatememo(self, node, type):
        if node != None:
            parent_id, date = self.nodeInfo(node, type)
            if parent_id == None or date == None:
                self.Tips("该节点无法添加")
                return
            data = {"id": str(uuid.uuid1()), "node_name": "(无标题)", "connect_date": date, "is_folder": 0,
                    "parent_id": parent_id, "memo_id": str(uuid.uuid1())}
            if type == "same":
                self.createNodeByDict(node.parent(), data)
            if type == "child":
                self.createNodeByDict(node, data)
            memoView = memoViewImpl()
            memoView.data = data
            self.mdiArea.addSubWindow(memoView)
            memoView.show()
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.Tips("未选择节点")

     # 编辑文件夹
    def editDir(self, node):
        try:
            if node != None:
                inputDialog = inputDialogImpl()
                if inputDialog.exec() == inputDialog.Accepted:
                    name = inputDialog.inputLineEdit.text()
                    id = node.data["id"]
                    sql = "Update t_base_node set node_name = ? where id = ?"
                    self.sqlite.execute(sql, [name, id])
                    node.setText(0, name)
            else:
                self.Tips("未选择节点")
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmemo.error(e)

    # 删除节点
    def deleteNode(self, node):
        while node.childCount() > 0:
            self.deleteNode(node.child(0))
        parent = node.parent()
        parent.removeChild(node)
        sql = "Delete from t_base_node where id = ?"
        self.sqlite.execute(sql, node.nodeData[""])
        if node.nodeData["memo_id"] != "":
            sql = "Delete from t_memo_detail where id = ?"
            self.sqlite.execute(sql, node.nodeData["memo_id"])

    # 节点信息检查
    def nodeInfo(self, node, type):
        parent_id, date = "",""
        if "unAddable"  not in node.sign:
            if type == "child":
                if "folder" in node.sign:
                    parent_id = node.id
                elif "date" in node.sign:
                    parent_id = "0"
            elif type == "same":
                if "folder" in node.parent().sign:
                    parent_id = node.parent().id
                elif "date" in node.parent().sign and "folder" in node.sign:
                    parent_id = "0"
            if hasattr(node, "date"):
                date = node.date
            elif hasattr(node, "data"):
                date = node.nodeData["connect_date"]
        return parent_id, date

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

    # 改变显示窗口
    def changeShow(self,node):
        if "file" in node.sign:
            memo = self.checkMemoOpen(node.nodeData["memo_id"])
            if memo is None:
                sql = "select memo_context from t_memo_detail where id = ?"
                datas = self.sqlite.executeQuery(sql, node.nodeData["memo_id"])
                memoView = memoViewImpl()
                if len(datas) == 1:
                    memoView.context = datas[0]["memo_context"]
                memoView.data = node.nodeData
                self.mdiArea.addSubWindow(memoView)
                memoView.show()
            else :
                self.mdiArea.setActiveSubWindow(memo)
            self.stackedWidget.setCurrentIndex(1)
        elif "folder" in node.sign:
            sql = "select memo_id,node_name,memo_temp from v_memo_list where parent_id = ?"
            datas = self.sqlite.executeQuery(sql, node.nodeData["id"])
            self.tableShow(datas)
            self.dirLabel.setText(node.text(0))
            self.countLabel.setText(str(len(datas)))
            self.stackedWidget.setCurrentIndex(0)
        elif "date" in node.sign and hasattr(node, "date"):
            sql = "select memo_id,node_name,memo_temp from v_memo_list where connect_date = ?"
            datas = self.sqlite.executeQuery(sql, node.date)
            self.dirLabel.setText(node.date)
            self.countLabel.setText(str(len(datas)))
            self.tableShow(datas)
            self.stackedWidget.setCurrentIndex(0)
        else:
            return

    # 检查是否已开启备忘
    def checkMemoOpen(self,id):
        if len(self.mdiArea.subWindowList()) > 0:
            for window in self.mdiArea.subWindowList() :
                if window.widget().data["memo_id"] == id :
                    return window
        return None


    # 表格填充数据
    def tableShow(self,datas):
        for data in datas:
            rowPosition = self.fileTableWidget.rowCount()
            self.fileTableWidget.insertRow(rowPosition)
            i = 0
            for value in data:
                self.fileTableWidget.setItem(rowPosition, i, QTableWidgetItem(value))
                i += 1

    # 表格打开日志
    def tableOpenMemo(self):
        if self.tableWidget.currentIndex().row() == -1:
            return
        else:
            index = self.tableWidget.currentIndex().row()
        id = self.tableWidget.item(index, 0).text()
        sql = "select memo_context from t_memo_detail"
        datas = self.sqlite.executeQuery(sql, id)
        memoView = memoViewImpl()
        if len(datas) == 1:
            memoView.context = datas[0]["memo_context"]
        self.mdiArea.addSubWindow(memoView)
        self.stackedWidget.setCurrentIndex(1)

    #检查是否有窗体
    def windowCheck(self):
        window = self.mdiArea.activeSubWindow()
        if window is None :
            return False
        else:
            return True

    #文件字体颜色
    def fileColorBox(self):
        if self.windowCheck():
            col = QColorDialog.getColor()
            if col.isValid():
                self.mdiArea.activeSubWindow().widget().textEdit.setTextColor(col)

    #字体局左
    def alignLeft(self):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.setAlignment(Qt.AlignLeft)

    # 字体局中
    def alignCenter(self):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.setAlignment(Qt.AlignCenter)

    # 字体局左
    def alignRight(self):
        self.mdiArea.activeSubWindow().widget().textEdit.setAlignment(Qt.AlignLeft)
