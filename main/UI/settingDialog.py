# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
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
"border-radius:8px\n"
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
        self.closePushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.closePushButton.setMaximumSize(QtCore.QSize(16, 16))
        self.closePushButton.setStyleSheet("QPushButton{\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::hover{\n"
"    background:#aa3e3e;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}\n"
"")
        self.closePushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label_6 = QtWidgets.QLabel(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.todoOnButton = QtWidgets.QRadioButton(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.todoOnButton.setFont(font)
        self.todoOnButton.setObjectName("todoOnButton")
        self.buttonGroup = QtWidgets.QButtonGroup(settingDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.todoOnButton)
        self.horizontalLayout_4.addWidget(self.todoOnButton)
        self.todoOffButton = QtWidgets.QRadioButton(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.todoOffButton.setFont(font)
        self.todoOffButton.setObjectName("todoOffButton")
        self.buttonGroup.addButton(self.todoOffButton)
        self.horizontalLayout_4.addWidget(self.todoOffButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_8 = QtWidgets.QLabel(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.autoOnButton = QtWidgets.QRadioButton(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.autoOnButton.setFont(font)
        self.autoOnButton.setObjectName("autoOnButton")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(settingDialog)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.autoOnButton)
        self.horizontalLayout_5.addWidget(self.autoOnButton)
        self.autoOffButton = QtWidgets.QRadioButton(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.autoOffButton.setFont(font)
        self.autoOffButton.setObjectName("autoOffButton")
        self.buttonGroup_3.addButton(self.autoOffButton)
        self.horizontalLayout_5.addWidget(self.autoOffButton)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label_3 = QtWidgets.QLabel(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.closeTipOnButton = QtWidgets.QRadioButton(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.closeTipOnButton.setFont(font)
        self.closeTipOnButton.setObjectName("closeTipOnButton")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(settingDialog)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.closeTipOnButton)
        self.horizontalLayout_6.addWidget(self.closeTipOnButton)
        self.closeTipOffButton = QtWidgets.QRadioButton(self.sysTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.closeTipOffButton.setFont(font)
        self.closeTipOffButton.setObjectName("closeTipOffButton")
        self.buttonGroup_4.addButton(self.closeTipOffButton)
        self.horizontalLayout_6.addWidget(self.closeTipOffButton)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
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
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.tabWidget.addTab(self.sysTab, "")
        self.safeTab = QtWidgets.QWidget()
        self.safeTab.setStyleSheet("QWidget>QLineEdit{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}")
        self.safeTab.setObjectName("safeTab")
        self.formLayout_3 = QtWidgets.QFormLayout(self.safeTab)
        self.formLayout_3.setContentsMargins(15, -1, 15, -1)
        self.formLayout_3.setHorizontalSpacing(3)
        self.formLayout_3.setVerticalSpacing(15)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.safeTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sysLockOnButton = QtWidgets.QRadioButton(self.safeTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.sysLockOnButton.setFont(font)
        self.sysLockOnButton.setObjectName("sysLockOnButton")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(settingDialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.sysLockOnButton)
        self.horizontalLayout_2.addWidget(self.sysLockOnButton)
        self.sysLockOffButton = QtWidgets.QRadioButton(self.safeTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.sysLockOffButton.setFont(font)
        self.sysLockOffButton.setObjectName("sysLockOffButton")
        self.buttonGroup_2.addButton(self.sysLockOffButton)
        self.horizontalLayout_2.addWidget(self.sysLockOffButton)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.safeTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sysLockPassEdit = QtWidgets.QLineEdit(self.safeTab)
        self.sysLockPassEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sysLockPassEdit.setObjectName("sysLockPassEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sysLockPassEdit)
        self.tabWidget.addTab(self.safeTab, "")
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
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.gitNameLabel)
        self.davNameEdit = QtWidgets.QLineEdit(self.gitTab)
        self.davNameEdit.setObjectName("davNameEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.davNameEdit)
        self.gitPasswordLabel = QtWidgets.QLabel(self.gitTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.gitPasswordLabel.setFont(font)
        self.gitPasswordLabel.setObjectName("gitPasswordLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.gitPasswordLabel)
        self.davPasswordEdit = QtWidgets.QLineEdit(self.gitTab)
        self.davPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.davPasswordEdit.setObjectName("davPasswordEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.davPasswordEdit)
        self.gitProgramLabel = QtWidgets.QLabel(self.gitTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.gitProgramLabel.setFont(font)
        self.gitProgramLabel.setObjectName("gitProgramLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.gitProgramLabel)
        self.davUrlEdit = QtWidgets.QLineEdit(self.gitTab)
        self.davUrlEdit.setObjectName("davUrlEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.davUrlEdit)
        self.label_10 = QtWidgets.QLabel(self.gitTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.davOnButton = QtWidgets.QRadioButton(self.gitTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.davOnButton.setFont(font)
        self.davOnButton.setObjectName("davOnButton")
        self.horizontalLayout_7.addWidget(self.davOnButton)
        self.davOffButton = QtWidgets.QRadioButton(self.gitTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.davOffButton.setFont(font)
        self.davOffButton.setObjectName("davOffButton")
        self.horizontalLayout_7.addWidget(self.davOffButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_11 = QtWidgets.QLabel(self.gitTab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_11)
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
        self.label_6.setText(_translate("settingDialog", "桌面任务："))
        self.todoOnButton.setText(_translate("settingDialog", "启用"))
        self.todoOffButton.setText(_translate("settingDialog", "禁用"))
        self.label_8.setText(_translate("settingDialog", "开机自启动："))
        self.label_9.setText(_translate("settingDialog", "关闭确认："))
        self.autoOnButton.setText(_translate("settingDialog", "是"))
        self.autoOffButton.setText(_translate("settingDialog", "否"))
        self.label_3.setText(_translate("settingDialog", "番茄币换算："))
        self.closeTipOnButton.setText(_translate("settingDialog", "开启"))
        self.closeTipOffButton.setText(_translate("settingDialog", "关闭"))
        self.label_4.setText(_translate("settingDialog", "1元相当于"))
        self.label_5.setText(_translate("settingDialog", "个番茄币"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sysTab), _translate("settingDialog", "系统设置"))
        self.label_7.setText(_translate("settingDialog", "系统锁："))
        self.sysLockOnButton.setText(_translate("settingDialog", "开启"))
        self.sysLockOffButton.setText(_translate("settingDialog", "关闭"))
        self.label_2.setText(_translate("settingDialog", "密码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.safeTab), _translate("settingDialog", "安全设置"))
        self.gitNameLabel.setText(_translate("settingDialog", "用户名："))
        self.gitPasswordLabel.setText(_translate("settingDialog", "密码："))
        self.gitProgramLabel.setText(_translate("settingDialog", "网盘地址："))
        self.label_10.setText(_translate("settingDialog", "启用备份："))
        self.davOnButton.setText(_translate("settingDialog", "启用"))
        self.davOffButton.setText(_translate("settingDialog", "禁用"))
        self.label_11.setText(_translate("settingDialog", "如果是坚果云，似乎/dav/这个文件夹不能访问，在下面再建一个文件夹，比如backup。坚果云密码为应用密码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gitTab), _translate("settingDialog", "webDav同步"))

import UI.icons_rc
