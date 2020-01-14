# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settingDialog(object):
    def setupUi(self, settingDialog):
        settingDialog.setObjectName("settingDialog")
        settingDialog.resize(415, 288)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.verticalLayout = QtWidgets.QVBoxLayout(settingDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowBar = QtWidgets.QWidget(settingDialog)
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
        spacerItem = QtWidgets.QSpacerItem(217, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.windowBar)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(216, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.closePushButton = QtWidgets.QPushButton(self.windowBar)
        self.closePushButton.setMinimumSize(QtCore.QSize(20, 20))
        self.closePushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.closePushButton.setStyleSheet("background:#F95D5C;")
        self.closePushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/close_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closePushButton.setIcon(icon)
        self.closePushButton.setIconSize(QtCore.QSize(10, 10))
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout.addWidget(self.closePushButton)
        self.verticalLayout.addWidget(self.windowBar)
        self.mainWidget = QtWidgets.QWidget(settingDialog)
        self.mainWidget.setStyleSheet("QWidget#mainWidget{\n"
"    background:#e9eaed;\n"
"    border-bottom:1px solid gray;\n"
"    border-right:1px solid gray;\n"
"    border-left:1px solid gray;\n"
"    border-bottom-left-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"}\n"
"QDialogButtonBox>QPushButton{\n"
"    background:#656565;\n"
"    color:#FEFEFE;\n"
"    font: 9pt \"Microsoft YaHei UI\";\n"
"    border-radius:4px;\n"
"    width:60px;\n"
"    height:24px;\n"
"    margin-top:3px;\n"
"    margin-right:8px;\n"
"}\n"
"QDialogButtonBox>QPushButton:checked{\n"
"    background:#FEFEFE;\n"
"    color:#656565;\n"
"}\n"
"")
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_2.setContentsMargins(1, 0, 1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.mainWidget)
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
"#tab,#tab_2,#tab_3,#tab_4{\n"
"    background:#E9EAED;\n"
"}\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.sysTab = QtWidgets.QWidget()
        self.sysTab.setStyleSheet("QWidget>QLineEdit{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"")
        self.sysTab.setObjectName("sysTab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.sysTab)
        self.formLayout_2.setContentsMargins(15, -1, 15, -1)
        self.formLayout_2.setHorizontalSpacing(3)
        self.formLayout_2.setVerticalSpacing(15)
        self.formLayout_2.setObjectName("formLayout_2")
        self.gitNameLabel_2 = QtWidgets.QLabel(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.gitNameLabel_2.setFont(font)
        self.gitNameLabel_2.setObjectName("gitNameLabel_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.gitNameLabel_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sysLockOnButton = QtWidgets.QRadioButton(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.sysLockOnButton.setFont(font)
        self.sysLockOnButton.setObjectName("sysLockOnButton")
        self.buttonGroup = QtWidgets.QButtonGroup(settingDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.sysLockOnButton)
        self.horizontalLayout_2.addWidget(self.sysLockOnButton)
        self.sysLockOffButton = QtWidgets.QRadioButton(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.sysLockOffButton.setFont(font)
        self.sysLockOffButton.setObjectName("sysLockOffButton")
        self.buttonGroup.addButton(self.sysLockOffButton)
        self.horizontalLayout_2.addWidget(self.sysLockOffButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sysLockPassEdit = QtWidgets.QLineEdit(self.sysTab)
        self.sysLockPassEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sysLockPassEdit.setObjectName("sysLockPassEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sysLockPassEdit)
        self.label_3 = QtWidgets.QLabel(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.tomatoRateSpinBox = QtWidgets.QDoubleSpinBox(self.sysTab)
        self.tomatoRateSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.tomatoRateSpinBox.setStyleSheet("QSpinBox,QDoubleSpinBox{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"/*spinbox 抬起样式*/\n"
"QDoubleSpinBox::up-button,QSpinBox::up-button {\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"    image: url(:/icon/add.png);\n"
"    width: 16px;\n"
"    height: 20px;       \n"
"}\n"
"QDoubleSpinBox::down-button,QSpinBox::down-button {\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"    border-image: url(:/icon/remove.png);\n"
"    width: 16px;\n"
"    height: 17px;\n"
"}\n"
"/*按钮按下样式*/\n"
"QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"    image: url(:/icon/add.png);\n"
"    width: 16px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"    image: url(:/icon/remove.png);\n"
"    width: 16px;\n"
"    height: 17px;\n"
"}")
        self.tomatoRateSpinBox.setObjectName("tomatoRateSpinBox")
        self.horizontalLayout_3.addWidget(self.tomatoRateSpinBox)
        self.label_5 = QtWidgets.QLabel(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_6 = QtWidgets.QLabel(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.todoOnButton = QtWidgets.QRadioButton(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.todoOnButton.setFont(font)
        self.todoOnButton.setObjectName("todoOnButton")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(settingDialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.todoOnButton)
        self.horizontalLayout_4.addWidget(self.todoOnButton)
        self.todoOffButton = QtWidgets.QRadioButton(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.todoOffButton.setFont(font)
        self.todoOffButton.setObjectName("todoOffButton")
        self.buttonGroup_2.addButton(self.todoOffButton)
        self.horizontalLayout_4.addWidget(self.todoOffButton)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.tabWidget.addTab(self.sysTab, "")
        self.gitTab = QtWidgets.QWidget()
        self.gitTab.setStyleSheet("QWidget>QLineEdit{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}")
        self.gitTab.setObjectName("gitTab")
        self.formLayout = QtWidgets.QFormLayout(self.gitTab)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(15, -1, 15, -1)
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.gitNameLabel = QtWidgets.QLabel(self.gitTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.gitNameLabel.setFont(font)
        self.gitNameLabel.setObjectName("gitNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.gitNameLabel)
        self.gitPasswordLabel = QtWidgets.QLabel(self.gitTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.gitPasswordLabel.setFont(font)
        self.gitPasswordLabel.setObjectName("gitPasswordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.gitPasswordLabel)
        self.gitProgramLabel = QtWidgets.QLabel(self.gitTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.gitProgramLabel.setFont(font)
        self.gitProgramLabel.setObjectName("gitProgramLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.gitProgramLabel)
        self.gitNameEdit = QtWidgets.QLineEdit(self.gitTab)
        self.gitNameEdit.setObjectName("gitNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.gitNameEdit)
        self.gitPasswordEdit = QtWidgets.QLineEdit(self.gitTab)
        self.gitPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gitPasswordEdit.setObjectName("gitPasswordEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gitPasswordEdit)
        self.gitProgramEdit = QtWidgets.QLineEdit(self.gitTab)
        self.gitProgramEdit.setObjectName("gitProgramEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gitProgramEdit)
        self.linkLabel = QtWidgets.QLabel(self.gitTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.linkLabel.setFont(font)
        self.linkLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.linkLabel.setObjectName("linkLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.linkLabel)
        self.linkShowLabel = QtWidgets.QLabel(self.gitTab)
        self.linkShowLabel.setMinimumSize(QtCore.QSize(0, 60))
        self.linkShowLabel.setMaximumSize(QtCore.QSize(340, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.linkShowLabel.setFont(font)
        self.linkShowLabel.setText("")
        self.linkShowLabel.setTextFormat(QtCore.Qt.PlainText)
        self.linkShowLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.linkShowLabel.setWordWrap(True)
        self.linkShowLabel.setObjectName("linkShowLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.linkShowLabel)
        self.tabWidget.addTab(self.gitTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.mainWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("取消")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Save).setText("保存")
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.mainWidget)
        self.verticalLayout.setStretch(1, 9)

        self.retranslateUi(settingDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.rejected.connect(settingDialog.reject)
        self.closePushButton.clicked.connect(settingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(settingDialog)

    def retranslateUi(self, settingDialog):
        _translate = QtCore.QCoreApplication.translate
        settingDialog.setWindowTitle(_translate("settingDialog", "Dialog"))
        self.label.setText(_translate("settingDialog", "系统设置"))
        self.gitNameLabel_2.setText(_translate("settingDialog", "系统锁："))
        self.sysLockOnButton.setText(_translate("settingDialog", "开启"))
        self.sysLockOffButton.setText(_translate("settingDialog", "关闭"))
        self.label_2.setText(_translate("settingDialog", "密码："))
        self.label_3.setText(_translate("settingDialog", "番茄币换算："))
        self.label_4.setText(_translate("settingDialog", "1元相当于"))
        self.label_5.setText(_translate("settingDialog", "个番茄币"))
        self.label_6.setText(_translate("settingDialog", "桌面任务："))
        self.todoOnButton.setText(_translate("settingDialog", "启用"))
        self.todoOffButton.setText(_translate("settingDialog", "禁用"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sysTab), _translate("settingDialog", "系统设置"))
        self.gitNameLabel.setText(_translate("settingDialog", "github用户名："))
        self.gitPasswordLabel.setText(_translate("settingDialog", "github密码："))
        self.gitProgramLabel.setText(_translate("settingDialog", "创建项目名："))
        self.linkLabel.setText(_translate("settingDialog", "生成的链接串："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gitTab), _translate("settingDialog", "github信息"))

import UI.icons_rc
