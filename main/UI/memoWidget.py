# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memoWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_memoWidget(object):
    def setupUi(self, memoWidget):
        memoWidget.setObjectName("memoWidget")
        memoWidget.resize(886, 541)
        self.horizontalLayout = QtWidgets.QHBoxLayout(memoWidget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(memoWidget)
        self.calendarWidget.setMinimumSize(QtCore.QSize(240, 200))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("/*顶部导航区域*/\n"
"#qt_calendar_navigationbar {\n"
"    background-color: #F95D5C;\n"
"    min-height: 30px;\n"
"}\n"
"/*上一个月按钮和下一个月按钮(从源码里找到的objectName)*/\n"
"#qt_calendar_prevmonth, #qt_calendar_nextmonth {\n"
"    border: none; /*去掉边框*/\n"
"    /*margin-top: 64px;*/\n"
"    color: white;\n"
"    min-width: 24px;\n"
"    max-width: 24px;\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"    border-radius: 12px; /*看来近似椭圆*/\n"
"    font-weight: bold; /*字体加粗*/\n"
"    qproperty-icon: none; /*去掉默认的方向键图片，当然也可以自定义*/\n"
"    background-color: transparent;/*背景颜色透明*/\n"
"}\n"
"#qt_calendar_prevmonth {\n"
"    qproperty-text: \"<\"; /*修改按钮的文字*/\n"
"}\n"
"#qt_calendar_nextmonth {\n"
"    qproperty-text: \">\";\n"
"}\n"
"#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {\n"
"    background-color: rgba(225, 225, 225, 100);\n"
"}\n"
"#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"\n"
"/*年,月控件*/\n"
"#qt_calendar_yearbutton, #qt_calendar_monthbutton {\n"
"    color: white;\n"
"    /*margin: 18px;*/\n"
"    min-width: 60px;\n"
"    border-radius: 8px;\n"
"}\n"
"#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {\n"
"    background-color: rgba(225, 225, 225, 100);\n"
"}\n"
"#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"\n"
"/*年份输入框*/\n"
"#qt_calendar_yearedit {\n"
"    min-width: 50px;\n"
"    color: white;\n"
"    background: transparent;/*让输入框背景透明*/\n"
"}\n"
"#qt_calendar_yearedit::up-button { /*往上的按钮*/\n"
"    width: 20px;\n"
"    subcontrol-position: right;/*移动到右边*/\n"
"}\n"
"#qt_calendar_yearedit::down-button { /*往下的按钮*/\n"
"    width: 20px;\n"
"    subcontrol-position: left; /*移动到左边去*/\n"
"}\n"
"\n"
"\n"
"/*月份选择菜单*/\n"
"CalendarWidget>QToolButton>QMenu {\n"
"     background-color: white;\n"
"}\n"
"CalendarWidget QToolButton QMenu::item {\n"
"    padding: 10px;\n"
"}\n"
"CalendarWidget>QToolButton>QMenu::item:selected:enabled {\n"
"    background-color: #F95D5C;\n"
"}\n"
"CalendarWidget QToolButton::menu-indicator {\n"
"    /*image: none;去掉月份选择下面的小箭头*/\n"
"    subcontrol-position: right top;/*右边居中*/\n"
"}\n"
"\n"
"\n"
"/*下方的日历表格*/\n"
"#qt_calendar_calendarview {\n"
"    outline: 0px;/*去掉选中后的虚线框*/\n"
"    selection-background-color: #F95D5C; /*选中背景颜色*/\n"
"}\n"
"\n"
"")
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.docListWidget = QtWidgets.QWidget(memoWidget)
        self.docListWidget.setObjectName("docListWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.docListWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.docListWidget)
        self.widget.setStyleSheet("QWidget>QPushButton{\n"
"    background-color: #d1d1d1;\n"
"    border-radius:3px;\n"
"}\n"
"QWidget>QPushButton:hover{\n"
"    background-color: #ababab;\n"
"}\n"
"QWidget>QPushButton:pressed{\n"
"    background-color: #ababab;\n"
"    background:#c0d5d6;\n"
"}\n"
"QWidget>QToolButton{\n"
"    background-color: #d1d1d1;\n"
"    border-radius:3px;\n"
"}\n"
"QWidget>QToolButton:hover{\n"
"    background-color: #ababab;\n"
"}\n"
"QWidget>QToolButton:pressed{\n"
"    background-color: #ababab;\n"
"    background:#c0d5d6;\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.addTodayButton = QtWidgets.QPushButton(self.widget)
        self.addTodayButton.setMinimumSize(QtCore.QSize(80, 25))
        self.addTodayButton.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.addTodayButton.setFont(font)
        self.addTodayButton.setObjectName("addTodayButton")
        self.horizontalLayout_4.addWidget(self.addTodayButton)
        self.showMenuButton = QtWidgets.QToolButton(self.widget)
        self.showMenuButton.setMinimumSize(QtCore.QSize(25, 25))
        self.showMenuButton.setMaximumSize(QtCore.QSize(25, 25))
        self.showMenuButton.setStyleSheet("QToolButton::menu-indicator { image: None; }")
        self.showMenuButton.setText("")
        self.showMenuButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.showMenuButton.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.showMenuButton.setAutoRaise(True)
        self.showMenuButton.setArrowType(QtCore.Qt.DownArrow)
        self.showMenuButton.setObjectName("showMenuButton")
        self.horizontalLayout_4.addWidget(self.showMenuButton)
        self.verticalLayout_3.addWidget(self.widget)
        self.treeWidget = QtWidgets.QTreeWidget(self.docListWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.setFont(font)
        self.treeWidget.setStyleSheet("QTreeWidget{\n"
"    border:none;\n"
"    background-color: rgba(209, 209, 209, 0);\n"
"}")
        self.treeWidget.setAutoScrollMargin(8)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.treeWidget)
        self.verticalLayout.addWidget(self.docListWidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(memoWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dirLabel = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.dirLabel.setFont(font)
        self.dirLabel.setText("")
        self.dirLabel.setObjectName("dirLabel")
        self.horizontalLayout_5.addWidget(self.dirLabel)
        self.label_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.countLabel = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.countLabel.setFont(font)
        self.countLabel.setObjectName("countLabel")
        self.horizontalLayout_5.addWidget(self.countLabel)
        self.label_5 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.fileTableWidget = QtWidgets.QTableWidget(self.page)
        self.fileTableWidget.setStyleSheet("QHeaderView::section{\n"
"    background: rgba(209, 209, 209, 90);\n"
"}")
        self.fileTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fileTableWidget.setAlternatingRowColors(True)
        self.fileTableWidget.setShowGrid(True)
        self.fileTableWidget.setObjectName("fileTableWidget")
        self.fileTableWidget.setColumnCount(3)
        self.fileTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.fileTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileTableWidget.setHorizontalHeaderItem(2, item)
        self.fileTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.fileTableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.fileTableWidget)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.page_2)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 29))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 29))
        self.widget_3.setStyleSheet("QWidget>QPushButton{\n"
"    border:none;\n"
"}\n"
"QWidget>QPushButton:hover{\n"
"    background:#c0d5d6;\n"
"}\n"
"QWidget>QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#c0d5d6;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(5, 2, 5, 2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.saveButton = QtWidgets.QPushButton(self.widget_3)
        self.saveButton.setMinimumSize(QtCore.QSize(25, 25))
        self.saveButton.setMaximumSize(QtCore.QSize(25, 25))
        self.saveButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.line = QtWidgets.QFrame(self.widget_3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.copyButton = QtWidgets.QPushButton(self.widget_3)
        self.copyButton.setMinimumSize(QtCore.QSize(25, 25))
        self.copyButton.setMaximumSize(QtCore.QSize(25, 25))
        self.copyButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copyButton.setIcon(icon1)
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout_2.addWidget(self.copyButton)
        self.cutButton = QtWidgets.QPushButton(self.widget_3)
        self.cutButton.setMinimumSize(QtCore.QSize(25, 25))
        self.cutButton.setMaximumSize(QtCore.QSize(25, 25))
        self.cutButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cutButton.setIcon(icon2)
        self.cutButton.setObjectName("cutButton")
        self.horizontalLayout_2.addWidget(self.cutButton)
        self.pasteButton = QtWidgets.QPushButton(self.widget_3)
        self.pasteButton.setMinimumSize(QtCore.QSize(25, 25))
        self.pasteButton.setMaximumSize(QtCore.QSize(25, 25))
        self.pasteButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pasteButton.setIcon(icon3)
        self.pasteButton.setObjectName("pasteButton")
        self.horizontalLayout_2.addWidget(self.pasteButton)
        self.line_2 = QtWidgets.QFrame(self.widget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.revokeButton = QtWidgets.QPushButton(self.widget_3)
        self.revokeButton.setMinimumSize(QtCore.QSize(25, 25))
        self.revokeButton.setMaximumSize(QtCore.QSize(25, 25))
        self.revokeButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/revoke.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.revokeButton.setIcon(icon4)
        self.revokeButton.setObjectName("revokeButton")
        self.horizontalLayout_2.addWidget(self.revokeButton)
        self.resumeButton = QtWidgets.QPushButton(self.widget_3)
        self.resumeButton.setMinimumSize(QtCore.QSize(25, 25))
        self.resumeButton.setMaximumSize(QtCore.QSize(25, 25))
        self.resumeButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/resume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resumeButton.setIcon(icon5)
        self.resumeButton.setObjectName("resumeButton")
        self.horizontalLayout_2.addWidget(self.resumeButton)
        self.fontComboBox = QtWidgets.QFontComboBox(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.fontComboBox.setFont(font)
        self.fontComboBox.setMaxCount(2147483646)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_2.addWidget(self.fontComboBox)
        self.fontSizeBox = QtWidgets.QSpinBox(self.widget_3)
        self.fontSizeBox.setMinimumSize(QtCore.QSize(40, 23))
        self.fontSizeBox.setProperty("value", 9)
        self.fontSizeBox.setObjectName("fontSizeBox")
        self.horizontalLayout_2.addWidget(self.fontSizeBox)
        self.bordButton = QtWidgets.QPushButton(self.widget_3)
        self.bordButton.setMinimumSize(QtCore.QSize(25, 25))
        self.bordButton.setMaximumSize(QtCore.QSize(25, 25))
        self.bordButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bordButton.setIcon(icon6)
        self.bordButton.setObjectName("bordButton")
        self.horizontalLayout_2.addWidget(self.bordButton)
        self.ItalicButton = QtWidgets.QPushButton(self.widget_3)
        self.ItalicButton.setMinimumSize(QtCore.QSize(25, 25))
        self.ItalicButton.setMaximumSize(QtCore.QSize(25, 25))
        self.ItalicButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/Italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ItalicButton.setIcon(icon7)
        self.ItalicButton.setObjectName("ItalicButton")
        self.horizontalLayout_2.addWidget(self.ItalicButton)
        self.underlineButton = QtWidgets.QPushButton(self.widget_3)
        self.underlineButton.setMinimumSize(QtCore.QSize(25, 25))
        self.underlineButton.setMaximumSize(QtCore.QSize(25, 25))
        self.underlineButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underlineButton.setIcon(icon8)
        self.underlineButton.setObjectName("underlineButton")
        self.horizontalLayout_2.addWidget(self.underlineButton)
        self.line_3 = QtWidgets.QFrame(self.widget_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.leftJustButton = QtWidgets.QPushButton(self.widget_3)
        self.leftJustButton.setMinimumSize(QtCore.QSize(25, 25))
        self.leftJustButton.setMaximumSize(QtCore.QSize(25, 25))
        self.leftJustButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/leftJust.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftJustButton.setIcon(icon9)
        self.leftJustButton.setObjectName("leftJustButton")
        self.horizontalLayout_2.addWidget(self.leftJustButton)
        self.centerButton = QtWidgets.QPushButton(self.widget_3)
        self.centerButton.setMinimumSize(QtCore.QSize(25, 25))
        self.centerButton.setMaximumSize(QtCore.QSize(25, 25))
        self.centerButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.centerButton.setIcon(icon10)
        self.centerButton.setObjectName("centerButton")
        self.horizontalLayout_2.addWidget(self.centerButton)
        self.rightJustButton = QtWidgets.QPushButton(self.widget_3)
        self.rightJustButton.setMinimumSize(QtCore.QSize(25, 25))
        self.rightJustButton.setMaximumSize(QtCore.QSize(25, 25))
        self.rightJustButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/rightJust.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightJustButton.setIcon(icon11)
        self.rightJustButton.setObjectName("rightJustButton")
        self.horizontalLayout_2.addWidget(self.rightJustButton)
        self.line_4 = QtWidgets.QFrame(self.widget_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.fontColorButton = QtWidgets.QPushButton(self.widget_3)
        self.fontColorButton.setMinimumSize(QtCore.QSize(25, 25))
        self.fontColorButton.setMaximumSize(QtCore.QSize(25, 25))
        self.fontColorButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon/fontColor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fontColorButton.setIcon(icon12)
        self.fontColorButton.setObjectName("fontColorButton")
        self.horizontalLayout_2.addWidget(self.fontColorButton)
        self.signlePenButton = QtWidgets.QPushButton(self.widget_3)
        self.signlePenButton.setMinimumSize(QtCore.QSize(25, 25))
        self.signlePenButton.setMaximumSize(QtCore.QSize(25, 25))
        self.signlePenButton.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon/singlePen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signlePenButton.setIcon(icon13)
        self.signlePenButton.setObjectName("signlePenButton")
        self.horizontalLayout_2.addWidget(self.signlePenButton)
        self.line_5 = QtWidgets.QFrame(self.widget_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.searchChangeButton = QtWidgets.QPushButton(self.widget_3)
        self.searchChangeButton.setMinimumSize(QtCore.QSize(25, 25))
        self.searchChangeButton.setMaximumSize(QtCore.QSize(25, 25))
        self.searchChangeButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icon/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchChangeButton.setIcon(icon14)
        self.searchChangeButton.setObjectName("searchChangeButton")
        self.horizontalLayout_2.addWidget(self.searchChangeButton)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.searchWidget = QtWidgets.QWidget(self.page_2)
        self.searchWidget.setStyleSheet("QWidget>QLineEdit{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"QWidget>QPushButton{\n"
"    border:none;\n"
"}\n"
"QWidget>QPushButton:hover{\n"
"    background:#c0d5d6;\n"
"}\n"
"QWidget>QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#c0d5d6;\n"
"}")
        self.searchWidget.setObjectName("searchWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.searchWidget)
        self.horizontalLayout_3.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.searchLineEdit = QtWidgets.QLineEdit(self.searchWidget)
        self.searchLineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.searchLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout_3.addWidget(self.searchLineEdit)
        self.searchButton = QtWidgets.QPushButton(self.searchWidget)
        self.searchButton.setMinimumSize(QtCore.QSize(24, 24))
        self.searchButton.setMaximumSize(QtCore.QSize(24, 24))
        self.searchButton.setText("")
        self.searchButton.setIcon(icon14)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_3.addWidget(self.searchButton)
        self.verticalLayout_4.addWidget(self.searchWidget)
        self.mdiArea = QtWidgets.QMdiArea(self.page_2)
        self.mdiArea.setAutoFillBackground(False)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setDocumentMode(False)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout_4.addWidget(self.mdiArea)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout.setStretch(1, 9)

        self.retranslateUi(memoWidget)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(memoWidget)

    def retranslateUi(self, memoWidget):
        _translate = QtCore.QCoreApplication.translate
        memoWidget.setWindowTitle(_translate("memoWidget", "Form"))
        self.addTodayButton.setToolTip(_translate("memoWidget", "新增今日备忘"))
        self.addTodayButton.setText(_translate("memoWidget", "当日备忘"))
        self.showMenuButton.setToolTip(_translate("memoWidget", "菜单"))
        self.label_2.setText(_translate("memoWidget", "的备忘（共"))
        self.countLabel.setText(_translate("memoWidget", "0"))
        self.label_5.setText(_translate("memoWidget", "篇）"))
        item = self.fileTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("memoWidget", "id"))
        item = self.fileTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("memoWidget", "日期"))
        item = self.fileTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("memoWidget", "摘要"))
        self.saveButton.setToolTip(_translate("memoWidget", "保存"))
        self.fontSizeBox.setToolTip(_translate("memoWidget", "字体大小"))
        self.bordButton.setToolTip(_translate("memoWidget", "加粗"))
        self.ItalicButton.setToolTip(_translate("memoWidget", "斜体"))
        self.underlineButton.setToolTip(_translate("memoWidget", "xia下划线"))
        self.leftJustButton.setToolTip(_translate("memoWidget", "左对齐"))
        self.centerButton.setToolTip(_translate("memoWidget", "居中"))
        self.rightJustButton.setToolTip(_translate("memoWidget", "右对齐"))
        self.fontColorButton.setToolTip(_translate("memoWidget", "字体颜色"))
        self.signlePenButton.setToolTip(_translate("memoWidget", "记号笔"))
        self.searchChangeButton.setToolTip(_translate("memoWidget", "搜索"))
        self.searchLineEdit.setPlaceholderText(_translate("memoWidget", "关键词"))
        self.searchButton.setToolTip(_translate("memoWidget", "搜索"))
import UI.icons_rc
