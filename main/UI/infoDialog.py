# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(409, 246)
        InfoDialog.setMaximumSize(QtCore.QSize(16777215, 246))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.verticalLayout = QtWidgets.QVBoxLayout(InfoDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowBar = QtWidgets.QWidget(InfoDialog)
        self.windowBar.setStyleSheet("QWidget#windowBar{\n"
"background:gray;\n"
"border-top:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"border-top-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"}\n"
"#windowBar>QPushButton{\n"
"border-radius:10px\n"
"}")
        self.windowBar.setObjectName("windowBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.windowBar)
        self.horizontalLayout.setContentsMargins(7, 2, 7, 2)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.windowBar)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.closePushButton = QtWidgets.QPushButton(self.windowBar)
        self.closePushButton.setMinimumSize(QtCore.QSize(20, 20))
        self.closePushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.closePushButton.setStyleSheet("#closePushButton{\n"
"    background:#F95D5C;\n"
"}")
        self.closePushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/close_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closePushButton.setIcon(icon)
        self.closePushButton.setIconSize(QtCore.QSize(10, 10))
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout.addWidget(self.closePushButton)
        self.verticalLayout.addWidget(self.windowBar)
        self.mainWidget = QtWidgets.QWidget(InfoDialog)
        self.mainWidget.setMaximumSize(QtCore.QSize(16777215, 222))
        self.mainWidget.setStyleSheet("QWidget#mainWidget{\n"
"background:#e9eaed;\n"
"border-bottom:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}")
        self.mainWidget.setObjectName("mainWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainWidget)
        self.horizontalLayout_2.setContentsMargins(1, 0, 1, 1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.infoItemWidget = QtWidgets.QWidget(self.mainWidget)
        self.infoItemWidget.setStyleSheet("#infoItemWidget{\n"
"    background:#dedede;\n"
"    border-bottom-left-radius:7px;\n"
"}\n"
"#infoItemWidget>QPushButton{\n"
"    border:none;\n"
"}\n"
"#infoItemWidget>QPushButton:hover{\n"
"    background:#c0d5d6;\n"
"}\n"
"#infoItemWidget>QPushButton:checked{\n"
"    background:#c0d5d6;\n"
"}")
        self.infoItemWidget.setObjectName("infoItemWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.infoItemWidget)
        self.verticalLayout_2.setContentsMargins(1, -1, 1, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.funcPushButton = QtWidgets.QPushButton(self.infoItemWidget)
        self.funcPushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.funcPushButton.setFont(font)
        self.funcPushButton.setObjectName("funcPushButton")
        self.verticalLayout_2.addWidget(self.funcPushButton)
        self.infoPushButton = QtWidgets.QPushButton(self.infoItemWidget)
        self.infoPushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.infoPushButton.setFont(font)
        self.infoPushButton.setObjectName("infoPushButton")
        self.verticalLayout_2.addWidget(self.infoPushButton)
        self.publisnPushButton = QtWidgets.QPushButton(self.infoItemWidget)
        self.publisnPushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.publisnPushButton.setFont(font)
        self.publisnPushButton.setObjectName("publisnPushButton")
        self.verticalLayout_2.addWidget(self.publisnPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 342, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.infoItemWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.funcPage = QtWidgets.QWidget()
        self.funcPage.setObjectName("funcPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.funcPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.funcLabel = QtWidgets.QLabel(self.funcPage)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.funcLabel.setFont(font)
        self.funcLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.funcLabel.setWordWrap(True)
        self.funcLabel.setObjectName("funcLabel")
        self.verticalLayout_3.addWidget(self.funcLabel)
        self.stackedWidget.addWidget(self.funcPage)
        self.infoPage = QtWidgets.QWidget()
        self.infoPage.setObjectName("infoPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.infoPage)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.infoPage)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"    border: none;\n"
"}\n"
"QTabBar::tab {\n"
"    border: none;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    color: white;\n"
"    border: 1px solid #656565;\n"
"    background:#656565;\n"
"    height: 18px;\n"
"    min-width: 65px;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"}\n"
"QTabBar::tab:hover {\n"
"    color: #656565;\n"
"    background: #E9EAED;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    color: #656565;\n"
"    height: 25px;\n"
"    background: #E9EAED;\n"
"    border-bottom: 1px solid #E9EAED;\n"
"}\n"
"QTabBar::tab:!selected{\n"
"    margin-top:5px;\n"
"}\n"
"\n"
"QTabWidget::pane{\n"
"    border-top: 1px solid #656565;\n"
"    margin-top: -2px;\n"
"}\n"
"#tab,#tab_2,#tab_3,#tab_4,#tab_5{\n"
"    background:#E9EAED;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.publishLabel_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.publishLabel_2.setFont(font)
        self.publishLabel_2.setTextFormat(QtCore.Qt.AutoText)
        self.publishLabel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.publishLabel_2.setWordWrap(True)
        self.publishLabel_2.setObjectName("publishLabel_2")
        self.verticalLayout_6.addWidget(self.publishLabel_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.publishLabel_3 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.publishLabel_3.setFont(font)
        self.publishLabel_3.setTextFormat(QtCore.Qt.AutoText)
        self.publishLabel_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.publishLabel_3.setWordWrap(True)
        self.publishLabel_3.setObjectName("publishLabel_3")
        self.verticalLayout_7.addWidget(self.publishLabel_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.publishLabel_4 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.publishLabel_4.setFont(font)
        self.publishLabel_4.setTextFormat(QtCore.Qt.AutoText)
        self.publishLabel_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.publishLabel_4.setWordWrap(True)
        self.publishLabel_4.setObjectName("publishLabel_4")
        self.verticalLayout_8.addWidget(self.publishLabel_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.publishLabel_5 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.publishLabel_5.setFont(font)
        self.publishLabel_5.setTextFormat(QtCore.Qt.AutoText)
        self.publishLabel_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.publishLabel_5.setWordWrap(True)
        self.publishLabel_5.setObjectName("publishLabel_5")
        self.verticalLayout_9.addWidget(self.publishLabel_5)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.publishLabel_6 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.publishLabel_6.setFont(font)
        self.publishLabel_6.setTextFormat(QtCore.Qt.AutoText)
        self.publishLabel_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.publishLabel_6.setWordWrap(True)
        self.publishLabel_6.setObjectName("publishLabel_6")
        self.verticalLayout_10.addWidget(self.publishLabel_6)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.infoPage)
        self.publishPage = QtWidgets.QWidget()
        self.publishPage.setObjectName("publishPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.publishPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.publishLabel = QtWidgets.QLabel(self.publishPage)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.publishLabel.setFont(font)
        self.publishLabel.setTextFormat(QtCore.Qt.AutoText)
        self.publishLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.publishLabel.setWordWrap(True)
        self.publishLabel.setObjectName("publishLabel")
        self.verticalLayout_4.addWidget(self.publishLabel)
        self.stackedWidget.addWidget(self.publishPage)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 8)
        self.verticalLayout.addWidget(self.mainWidget)

        self.retranslateUi(InfoDialog)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.closePushButton.clicked.connect(InfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        _translate = QtCore.QCoreApplication.translate
        InfoDialog.setWindowTitle(_translate("InfoDialog", "Dialog"))
        self.label.setText(_translate("InfoDialog", "软件介绍"))
        self.funcPushButton.setText(_translate("InfoDialog", "软件功能"))
        self.infoPushButton.setText(_translate("InfoDialog", "使用说明"))
        self.publisnPushButton.setText(_translate("InfoDialog", "作者介绍"))
        self.funcLabel.setText(_translate("InfoDialog", "<html><head/><body><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;番茄农场是集番茄时钟，计划任务，时间规划于一身的软件，同时加入了番茄币和集市的概念，在有效的规划的时间同时，建立有效的激励机制，在市场设定自己想要的东西以及价格，通过完成任务来获取番茄币获取，既能培养习惯。</p></body></html>"))
        self.publishLabel_2.setText(_translate("InfoDialog", "<html><head/><body><p>任务箱中分配过的任务都会在这个页面显示，点击开始按钮即可开启任务番茄钟，点击删除按钮即可解除分配</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("InfoDialog", "首页"))
        self.publishLabel_3.setText(_translate("InfoDialog", "<html><head/><body><p>用户所有执行过的任务数据都会在这个页面进行体现</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("InfoDialog", "农场统计"))
        self.publishLabel_4.setText(_translate("InfoDialog", "<html><head/><body><p>创建的任务都会存放在任务箱中，可选择日期进行分配，分配过的任务就可以在主页开始执行</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("InfoDialog", "任务展板"))
        self.publishLabel_5.setText(_translate("InfoDialog", "<html><head/><body><p>可以根据日期创建相应的文件夹和备忘</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("InfoDialog", "日志备忘"))
        self.publishLabel_6.setText(_translate("InfoDialog", "<html><head/><body><p>可以发布自己的商品，通过完成任务获得的番茄币进行购买</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("InfoDialog", "番茄市场"))
        self.publishLabel.setText(_translate("InfoDialog", "<html><head/><body><p>作者：jaywatson</p><p>博客：www.nothingistrue.top</p><p>github:https://github.com/WatsonJay</p></body></html>"))
import UI.icons_rc
