# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 13:34
# @Author  : Jaywatson
# @File    : memoWidgetImpl.py
# @Soft    : tomato_farm
import uuid
from datetime import datetime

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QTextCursor, QPalette
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
        self.tempNodes = []  # 日历创建临时节点存储
        self.memoList = []
        self.yearDict = {}  # 年节点存储
        self.confmemo = log.getlogger('gui')
        self.sqlite = sqlite('./config/tomato.db')
        self.loadTree()
        self.createBtnMenu()
        # 日历功能
        self.calendarWidget.clicked.connect(self.dayDirCreate)
        self.addTodayButton.clicked.connect(self.todayMemo)
        # 文件树功能
        self.treeWidget.itemExpanded.connect(self.collapseOther)
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.createRightMenu)
        self.treeWidget.itemDoubleClicked.connect(self.changeShow)
        # 文件列表功能
        self.fileTableWidget.setColumnHidden(0, True)
        self.fileTableWidget.doubleClicked.connect(self.tableOpenMemo)
        # 文件编辑功能
        self.searchWidget.setVisible(False)
        self.copyButton.clicked.connect(self.fileCopy)
        self.cutButton.clicked.connect(self.fileCut)
        self.pasteButton.clicked.connect(self.filePaste)
        self.revokeButton.clicked.connect(self.fileUndo)
        self.resumeButton.clicked.connect(self.fileRedo)
        self.fontComboBox.currentFontChanged.connect(self.fileChangeFont)
        self.fontSizeBox.valueChanged.connect(self.fileChangeSize)
        self.leftJustButton.clicked.connect(self.alignLeft)
        self.centerButton.clicked.connect(self.alignCenter)
        self.rightJustButton.clicked.connect(self.alignRight)
        self.bordButton.clicked.connect(self.fileBold)
        self.ItalicButton.clicked.connect(self.fileItalic)
        self.underlineButton.clicked.connect(self.fileUnderline)
        self.fontColorButton.clicked.connect(self.fileColorBox)
        self.signlePenButton.clicked.connect(self.fileColorBackBox)
        self.searchChangeButton.clicked.connect(self.serchBarChange)
        self.searchButton.clicked.connect(self.fileSearch)
        self.searchLineEdit.returnPressed.connect(self.fileSearch)
        self.saveButton.clicked.connect(self.fileSave)

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
                memoNode = self.createNodeByDict(node.parent(), data)
            if type == "child":
                memoNode = self.createNodeByDict(node, data)
            self.memoList.append(memoNode)
            self.treeWidget.setCurrentItem(memoNode)
            memoView = memoViewImpl()
            memoView.data = data
            memoView.dateLabel.setText(data['connect_date'])
            self.mdiArea.addSubWindow(memoView)
            memoView.show()
            memoView.titleChangeSignal.connect(self.changeTitle)
            memoView.closeSignal.connect(self.fileSave)
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
        parent_id, date = "", ""
        if "unAddable" not in node.sign:
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

    # 创建当天目录
    def todayMemo(self):
        try:
            self.clearTempNode()
            date = datetime.now().strftime('%Y-%m-%d').split("-")
            dayNode = self.createDateNode(date[0], date[1], date[2])
            self.creatememo(dayNode, "child")
            self.tempNodes.clear()
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmemo.error(e)

    # 改变显示窗口
    def changeShow(self, node):
        try:
            if "file" in node.sign:
                memo = self.checkMemoOpen(node.nodeData["memo_id"])
                if memo is None:
                    sql = "select memo_context from t_memo_detail where id = ?"
                    datas = self.sqlite.executeQuery(sql, node.nodeData["memo_id"])
                    memoView = memoViewImpl()
                    memoView.data = node.nodeData
                    memoView.setWindowTitle(node.nodeData['node_name'])
                    memoView.title = node.nodeData['node_name']
                    memoView.titleLabel.setText(node.nodeData['node_name'])
                    memoView.dateLabel.setText(memoView.data['connect_date'])
                    if datas != None and len(datas) > 0:
                        memoView.textEdit.setHtml(datas[0]['memo_context'])
                    self.mdiArea.addSubWindow(memoView)
                    self.memoList.append(node)
                    memoView.show()
                    memoView.titleChangeSignal.connect(self.changeTitle)
                    memoView.closeSignal.connect(self.fileSave)
                else:
                    self.mdiArea.setActiveSubWindow(memo)
                self.stackedWidget.setCurrentIndex(1)
            elif "folder" in node.sign:
                sql = "select memo_id,node_name,connect_date,memo_temp from v_memo_list where parent_id = ?"
                datas = self.sqlite.executeQuery(sql, node.nodeData["id"])
                self.tableShow(datas)
                self.dirLabel.setText(node.text(0))
                self.countLabel.setText(str(len(datas)))
                self.stackedWidget.setCurrentIndex(0)
            elif "date" in node.sign and hasattr(node, "date"):
                sql = "select memo_id,node_name,connect_date,memo_temp from v_memo_list where connect_date = ?"
                datas = self.sqlite.executeQuery(sql, node.date)
                self.dirLabel.setText(node.date)
                self.countLabel.setText(str(len(datas)))
                self.tableShow(datas)
                self.stackedWidget.setCurrentIndex(0)
            else:
                return
        except Exception as e:
            self.Tips("系统异常，请查看日志")
            self.confmemo.error(e)

    # 修改标题
    def changeTitle(self, id, title):
        for memo in self.memoList:
            if memo.nodeData['id'] == id:
                memo.setText(0, title)
                memo.nodeData['node_name'] = title

    # 检查是否已开启备忘
    def checkMemoOpen(self, id):
        if len(self.mdiArea.subWindowList()) > 0:
            for window in self.mdiArea.subWindowList():
                if window.widget().data["memo_id"] == id:
                    return window
        return None

    # 表格填充数据
    def tableShow(self, datas):
        self.fileTableWidget.setRowCount(0)
        self.fileTableWidget.clearContents()
        for data in datas:
            rowPosition = self.fileTableWidget.rowCount()
            self.fileTableWidget.insertRow(rowPosition)
            i = 0
            for value in data:
                self.fileTableWidget.setItem(rowPosition, i, QTableWidgetItem(data[value]))
                i += 1

    # 表格打开日志
    def tableOpenMemo(self):
        if self.fileTableWidget.currentIndex().row() == -1:
            return
        else:
            index = self.fileTableWidget.currentIndex().row()
        id = self.fileTableWidget.item(index, 0).text()
        memo = self.checkMemoOpen(id)
        if memo is None:
            memoView = memoViewImpl()
            sql = "select memo_context from t_memo_detail where id = ?"
            datas = self.sqlite.executeQuery(sql, id)
            if datas != None and len(datas) > 0:
                memoView.textEdit.setHtml(datas[0]['memo_context'])
            sql = "select * from t_base_node where memo_id = ?"
            node = self.sqlite.executeQuery(sql,id)
            if node != None and len(node) > 0:
                memoView.data = node[0]
                memoView.setWindowTitle(memoView.data['node_name'])
                memoView.title = memoView.data['node_name']
                memoView.titleLabel.setText(memoView.data['node_name'])
                memoView.dateLabel.setText(memoView.data['connect_date'])
            self.mdiArea.addSubWindow(memoView)
            self.memoList.append(node)
            memoView.show()
            memoView.titleChangeSignal.connect(self.changeTitle)
            memoView.closeSignal.connect(self.fileSave)
        else:
            self.mdiArea.setActiveSubWindow(memo)
        self.stackedWidget.setCurrentIndex(1)

    # 检查是否有窗体
    def windowCheck(self):
        window = self.mdiArea.activeSubWindow()
        if window is None:
            return False
        else:
            return True

    # 复制
    def fileCopy(self):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.copy()

    # 剪切
    def fileCut(self):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.cut()

    # 粘贴
    def filePaste(self):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.paste()

    # 回退
    def fileUndo(self):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.undo()

    # 撤销
    def fileRedo(self):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.redo()

    # 字体变更
    def fileChangeFont(self, font):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.setCurrentFont(font)

    # 字体大小变更
    def fileChangeSize(self, size):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.setFontPointSize(size)

    # 字体局左
    def alignLeft(self):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.setAlignment(Qt.AlignLeft)

    # 字体局中
    def alignCenter(self):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.setAlignment(Qt.AlignCenter)

    # 字体局左
    def alignRight(self):
        if self.windowCheck():
            self.mdiArea.activeSubWindow().widget().textEdit.setAlignment(Qt.AlignRight)

    # 字体加粗
    def fileBold(self):
        if self.windowCheck():
            sub = self.mdiArea.activeSubWindow().widget().textEdit
            tmpFormat = sub.currentCharFormat()
            if tmpFormat.fontWeight() == QtGui.QFont.Bold:
                tmpFormat.setFontWeight(QtGui.QFont.Normal)
            else:
                tmpFormat.setFontWeight(QtGui.QFont.Bold)
            sub.mergeCurrentCharFormat(tmpFormat)

    # 字体斜体
    def fileItalic(self):
        if self.windowCheck():
            tmpTextBox = self.mdiArea.activeSubWindow().widget().textEdit
            tmpTextBox.setFontItalic(not tmpTextBox.fontItalic())

    # 字体下划线
    def fileUnderline(self):
        if self.windowCheck():
            tmpTextBox = self.mdiArea.activeSubWindow().widget().textEdit
            tmpTextBox.setFontUnderline(not tmpTextBox.fontUnderline())

    # 文件字体颜色
    def fileColorBox(self):
        if self.windowCheck():
            col = QColorDialog.getColor()
            if col.isValid():
                self.mdiArea.activeSubWindow().widget().textEdit.setTextColor(col)

    # 文件背景颜色
    def fileColorBackBox(self):
        if self.windowCheck():
            col = QColorDialog.getColor()
            if col.isValid():
                self.mdiArea.activeSubWindow().widget().textEdit.setTextBackgroundColor(col)

    # 搜索栏显示/隐藏
    def serchBarChange(self):
        visiable = self.searchWidget.isVisible()
        self.searchWidget.setVisible(not visiable)

    # 搜索
    def fileSearch(self):
        if self.windowCheck():
            keyWord = self.searchLineEdit.text()
            sub = self.mdiArea.activeSubWindow().widget()
            if sub.tempKeyWord != keyWord:
                sub.tempKeyWord = keyWord
                sub.textEdit.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
            if sub.textEdit.find(keyWord):
                palette = sub.textEdit.palette()
                palette.setColor(QPalette.Highlight, palette.color(QPalette.Active, QPalette.Highlight))
                sub.textEdit.setPalette(palette)
            else:
                sub.textEdit.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)

    def fileSave(self):
        if self.windowCheck():
            sub = self.mdiArea.activeSubWindow().widget()
            data = sub.data
            if data['node_name'] != '(无标题)' or data['node_name'] != '':
                sql = "replace into t_base_node (id,node_name,is_folder,parent_id,connect_date,memo_id) values (?,?,?,?,?,?)"
                self.sqlite.execute(sql, [data['id'], data['node_name'], data['is_folder'], data['parent_id'], data['connect_date'],data['memo_id']])
                sql = "replace into t_memo_detail (id, memo_context, memo_temp) values (?,?,?)"
                self.sqlite.execute(sql,[data['memo_id'],sub.textEdit.toHtml(),sub.textEdit.toPlainText()[:50]])
            else:
                self.Tips("请输入标题")

