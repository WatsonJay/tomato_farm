# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'marketWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_marketWidget(object):
    def setupUi(self, marketWidget):
        marketWidget.setObjectName("marketWidget")
        marketWidget.resize(886, 541)
        marketWidget.setWindowTitle("")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(marketWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(marketWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(marketWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.tomatoCoinLabel = QtWidgets.QLabel(marketWidget)
        self.tomatoCoinLabel.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tomatoCoinLabel.setFont(font)
        self.tomatoCoinLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tomatoCoinLabel.setObjectName("tomatoCoinLabel")
        self.horizontalLayout_4.addWidget(self.tomatoCoinLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(marketWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(marketWidget)
        self.listWidget.setStyleSheet("#listWidget{\n"
"    border:none;\n"
"    background-color: rgba(209, 209, 209, 90);\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(marketWidget)
        self.stackedWidget.setStyleSheet("QWidget>QLineEdit{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"QWidget>QTextEdit{\n"
"    border:1px solid gray;\n"
"    background:white;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"QWidget>QDateEdit{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"QWidget>QDateEdit::drop-down{\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-left-color: gray; \n"
"}\n"
"QWidget>QDateEdit::down-arrow{\n"
"    border-image:url(:/icon/down.png);\n"
"}\n"
"QWidget>QPushButton{\n"
"    border:none;\n"
"    color:white;\n"
"    border-radius:12px;\n"
"}\n"
"\n"
"QSpinBox,QDoubleSpinBox{\n"
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
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("")
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.page)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget.setSizeIncrement(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(134, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setMinimumSize(QtCore.QSize(80, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("QPushButton{\n"
"    background:#6CE872;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#53b357;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#53b357;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_5.addWidget(self.addButton)
        self.modifButton = QtWidgets.QPushButton(self.widget)
        self.modifButton.setMinimumSize(QtCore.QSize(80, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.modifButton.setFont(font)
        self.modifButton.setStyleSheet("QPushButton{\n"
"    background:#f5de6a;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#c5b355;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#c5b355;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modifButton.setIcon(icon1)
        self.modifButton.setObjectName("modifButton")
        self.horizontalLayout_5.addWidget(self.modifButton)
        self.deleteButton = QtWidgets.QPushButton(self.widget)
        self.deleteButton.setMinimumSize(QtCore.QSize(80, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("QPushButton{\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#aa3e3e;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#aa3e3e;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/delete_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon2)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_5.addWidget(self.deleteButton)
        self.verticalLayout_2.addWidget(self.widget)
        self.deleteWidget = QtWidgets.QWidget(self.page)
        self.deleteWidget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.deleteWidget.setStyleSheet("#deleteWidget{\n"
"    background:#adbbd4;\n"
"}")
        self.deleteWidget.setObjectName("deleteWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.deleteWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.deleteWidget)
        self.label_2.setMinimumSize(QtCore.QSize(162, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.deleteCommButton = QtWidgets.QPushButton(self.deleteWidget)
        self.deleteCommButton.setMinimumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.deleteCommButton.setFont(font)
        self.deleteCommButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#aa3e3e;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#aa3e3e;\n"
"}")
        self.deleteCommButton.setObjectName("deleteCommButton")
        self.horizontalLayout_2.addWidget(self.deleteCommButton)
        self.verticalLayout_2.addWidget(self.deleteWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(6, 6, 6, 3)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.commNameLabel = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.commNameLabel.setFont(font)
        self.commNameLabel.setText("")
        self.commNameLabel.setObjectName("commNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.commNameLabel)
        self.label_5 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.commPriceLabel = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.commPriceLabel.setFont(font)
        self.commPriceLabel.setText("")
        self.commPriceLabel.setObjectName("commPriceLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.commPriceLabel)
        self.label_7 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.priceToCoinLabel = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.priceToCoinLabel.setFont(font)
        self.priceToCoinLabel.setText("")
        self.priceToCoinLabel.setObjectName("priceToCoinLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.priceToCoinLabel)
        self.label_8 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.createTimeLabel = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.createTimeLabel.setFont(font)
        self.createTimeLabel.setText("")
        self.createTimeLabel.setObjectName("createTimeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.createTimeLabel)
        self.label_9 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.buyTimeLabel = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.buyTimeLabel.setFont(font)
        self.buyTimeLabel.setText("")
        self.buyTimeLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.buyTimeLabel.setObjectName("buyTimeLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buyTimeLabel)
        self.label_10 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_17 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.descLabel = QtWidgets.QLabel(self.page)
        self.descLabel.setMinimumSize(QtCore.QSize(0, 60))
        self.descLabel.setMaximumSize(QtCore.QSize(304, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.descLabel.setFont(font)
        self.descLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descLabel.setWordWrap(True)
        self.descLabel.setObjectName("descLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.descLabel)
        self.linkLabel = QtWidgets.QLabel(self.page)
        self.linkLabel.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.linkLabel.setFont(font)
        self.linkLabel.setText("")
        self.linkLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.linkLabel.setWordWrap(True)
        self.linkLabel.setOpenExternalLinks(True)
        self.linkLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.linkLabel.setObjectName("linkLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.linkLabel)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.buyButton = QtWidgets.QPushButton(self.page)
        self.buyButton.setMinimumSize(QtCore.QSize(80, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.buyButton.setFont(font)
        self.buyButton.setStyleSheet("QPushButton{\n"
"    background:#6CE872;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#53b357;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#53b357;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/shop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buyButton.setIcon(icon3)
        self.buyButton.setObjectName("buyButton")
        self.horizontalLayout.addWidget(self.buyButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("")
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, 2, -1, 2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(6, 6, 6, 3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_19 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.commNameLineEdit = QtWidgets.QLineEdit(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.commNameLineEdit.setFont(font)
        self.commNameLineEdit.setObjectName("commNameLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.commNameLineEdit)
        self.label_20 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_23 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.buyDateEdit = QtWidgets.QDateEdit(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.buyDateEdit.setFont(font)
        self.buyDateEdit.setCalendarPopup(True)
        self.buyDateEdit.setObjectName("buyDateEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buyDateEdit)
        self.label_24 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.yesRadioButton = QtWidgets.QRadioButton(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.yesRadioButton.setFont(font)
        self.yesRadioButton.setObjectName("yesRadioButton")
        self.horizontalLayout_8.addWidget(self.yesRadioButton)
        self.noRadioButton = QtWidgets.QRadioButton(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.noRadioButton.setFont(font)
        self.noRadioButton.setObjectName("noRadioButton")
        self.horizontalLayout_8.addWidget(self.noRadioButton)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.label_31 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_31.setObjectName("label_31")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.commPriceBox = QtWidgets.QDoubleSpinBox(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.commPriceBox.setFont(font)
        self.commPriceBox.setMaximum(9999.99)
        self.commPriceBox.setObjectName("commPriceBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.commPriceBox)
        self.descEdit = QtWidgets.QTextEdit(self.page_2)
        self.descEdit.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.descEdit.setFont(font)
        self.descEdit.setObjectName("descEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.descEdit)
        self.label_11 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.linkLineEdit = QtWidgets.QLineEdit(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.linkLineEdit.setFont(font)
        self.linkLineEdit.setObjectName("linkLineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.linkLineEdit)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.commitButton = QtWidgets.QPushButton(self.page_2)
        self.commitButton.setMinimumSize(QtCore.QSize(70, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.commitButton.setFont(font)
        self.commitButton.setStyleSheet("QPushButton{\n"
"    background:#6CE872;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#53b357;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#53b357;\n"
"}")
        self.commitButton.setObjectName("commitButton")
        self.horizontalLayout_7.addWidget(self.commitButton)
        self.cancleButton = QtWidgets.QPushButton(self.page_2)
        self.cancleButton.setMinimumSize(QtCore.QSize(70, 24))
        self.cancleButton.setStyleSheet("QPushButton{\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#aa3e3e;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#aa3e3e;\n"
"}")
        self.cancleButton.setObjectName("cancleButton")
        self.horizontalLayout_7.addWidget(self.cancleButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(marketWidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(marketWidget)

    def retranslateUi(self, marketWidget):
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("marketWidget", "<html><head/><body><p><img src=\":/icon/storage.png\" width=\"25\" height=\"25\"/></p></body></html>"))
        self.label_4.setText(_translate("marketWidget", "番茄币："))
        self.tomatoCoinLabel.setText(_translate("marketWidget", "0"))
        self.label.setText(_translate("marketWidget", "商品列表"))
        self.addButton.setText(_translate("marketWidget", "新增商品"))
        self.modifButton.setText(_translate("marketWidget", "修改商品"))
        self.deleteButton.setText(_translate("marketWidget", "删除商品"))
        self.label_2.setText(_translate("marketWidget", "该商品超出预期时间，是否删除？"))
        self.deleteCommButton.setText(_translate("marketWidget", "删除"))
        self.label_3.setText(_translate("marketWidget", "商品名称："))
        self.label_5.setText(_translate("marketWidget", "商品价格："))
        self.label_7.setText(_translate("marketWidget", "折算番茄币："))
        self.label_8.setText(_translate("marketWidget", "创建时间："))
        self.label_9.setText(_translate("marketWidget", "预期购买时间："))
        self.label_10.setText(_translate("marketWidget", "商品链接："))
        self.label_17.setText(_translate("marketWidget", "描述："))
        self.descLabel.setText(_translate("marketWidget", "<html><head/><body><p><br/></p></body></html>"))
        self.buyButton.setText(_translate("marketWidget", "购买"))
        self.label_19.setText(_translate("marketWidget", "商品名称："))
        self.label_20.setText(_translate("marketWidget", "商品价格："))
        self.label_23.setText(_translate("marketWidget", "预期购买时间："))
        self.buyDateEdit.setDisplayFormat(_translate("marketWidget", "yyyy-M-d"))
        self.label_24.setText(_translate("marketWidget", "是否提醒："))
        self.yesRadioButton.setText(_translate("marketWidget", "是"))
        self.noRadioButton.setText(_translate("marketWidget", "否"))
        self.label_31.setText(_translate("marketWidget", "描述："))
        self.label_11.setText(_translate("marketWidget", "商品链接："))
        self.commitButton.setText(_translate("marketWidget", "发布"))
        self.cancleButton.setText(_translate("marketWidget", "取消"))
import UI.icons_rc
