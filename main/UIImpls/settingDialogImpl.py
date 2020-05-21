# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 10:47
# @Author  : Jaywatson
# @File    : settingDialogImpl.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import QDialog, QMessageBox

from UI.settingDialog import Ui_settingDialog
from UIImpls.noBorderImpl import noBorderImpl
from UIImpls.tipImpl import tipImpl
from util.loadConf import config
from util.loadData import sqlite
from util.webDavService import webDavService
from util.winReg import winReg


class settingDialogImpl(QDialog, Ui_settingDialog, noBorderImpl, tipImpl):

    # 初始化
    def __init__(self, parent=None):
        super(settingDialogImpl, self).__init__(parent)
        self.setupUi(self)
        self.conf = config()
        self.reg = winReg()
        self.loadConf()
        self.buttonBox.accepted.connect(self.saveConf)
        self.sqlite = sqlite('/config/tomato.db')

    # 加载配置
    def loadConf(self):
        if self.conf.decrypt(self.conf.getOption('system', 'islock')) == "True":
            self.sysLockOnButton.setChecked(True)
        else:
            self.sysLockOffButton.setChecked(True)
        self.sysLockPassEdit.setText(self.conf.decrypt(self.conf.getOption('system', 'password')))
        self.tomatoRateSpinBox.setValue(float(self.conf.getOption('system', 'tomatorate')))
        if self.conf.getOption('system', 'todoshow') == "True":
            self.todoOnButton.setChecked(True)
        else:
            self.todoOffButton.setChecked(True)
        if self.conf.getOption('system', 'closeTip') == "True":
            self.closeTipOnButton.setChecked(True)
        else:
            self.closeTipOffButton.setChecked(True)
        try:
            if not self.autoOnButton.isChecked():
                self.conf.addoption('system', 'autoOn', "False")
        except:
            pass
        if self.conf.getOption('system', 'autoOn') == "True":
            self.autoOnButton.setChecked(True)
        else:
            self.autoOffButton.setChecked(True)
        if self.conf.getOption('webDav', 'enable') == "True":
            self.davOnButton.setChecked(True)
        else:
            self.davOffButton.setChecked(True)
        self.davNameEdit.setText(self.conf.decrypt(self.conf.getOption('webDav', 'username')))
        self.davPasswordEdit.setText(self.conf.decrypt(self.conf.getOption('webDav', 'password')))
        self.davUrlEdit.setText(self.conf.decrypt(self.conf.getOption('webDav', 'url')))

    # 保存配置
    def saveConf(self):
        if self.sysLockOnButton.isChecked():
            self.conf.addoption('system', 'islock', self.conf.encrypt("True"))
        else:
            self.conf.addoption('system', 'islock', self.conf.encrypt("False"))
        self.conf.addoption('system', 'password', self.conf.encrypt(self.sysLockPassEdit.text()))
        self.conf.addoption('system', 'tomatorate', str(self.tomatoRateSpinBox.value()))
        if self.todoOnButton.isChecked():
            self.conf.addoption('system', 'todoshow', "True")
        else:
            self.conf.addoption('system', 'todoshow', "False")
        if self.closeTipOnButton.isChecked():
            self.conf.addoption('system', 'closetip', "True")
        else:
            self.conf.addoption('system', 'closetip', "False")
        try:
            if self.autoOnButton.isChecked():
                if self.reg.checkName():
                    self.reg.deleteReg()
                self.reg.addReg()
                self.conf.addoption('system', 'autoon', "True")
            else:
                self.reg.deleteReg()
                self.conf.addoption('system', 'autoon', "False")
        except:
            self.conf.addoption('system', 'autoon', "False")
        if self.davOnButton.isChecked():
            webDav = webDavService()
            if self.chekDbUsed():
                webDav.download('/config/tomato.db')
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle('文件存在差异')
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setText("本地文件已被修改，与云端数据可能不符，可能数据丢失")
                msgBox.setInformativeText("你需要哪个操作？")
                yes = msgBox.addButton('覆盖本地', QMessageBox.YesRole)
                no = msgBox.addButton('覆盖云端', QMessageBox.NoRole)
                cancle = msgBox.addButton('取消', QMessageBox.RejectRole)
                msgBox.setDefaultButton(yes)
                reply = msgBox.exec()
                if reply == 0:
                    webDav.download('/config/tomato.db')
                    self.conf.addoption('webDav', 'enable', "True")
                elif reply == 1:
                    webDav.upload('/config/tomato.db')
                    self.conf.addoption('webDav', 'enable', "True")
                else:
                    self.conf.addoption('webDav', 'enable', "False")
                    self.davOffButton.isChecked()
        else:
            self.conf.addoption('webDav', 'enable', "False")
        self.conf.addoption('webDav', 'username', self.conf.encrypt(self.davNameEdit.text()))
        self.conf.addoption('webDav', 'password', self.conf.encrypt(self.davPasswordEdit.text()))
        self.conf.addoption('webDav', 'url', self.conf.encrypt(self.davUrlEdit.text()))
        self.accept()

    def chekDbUsed(self):
        sql = "select * from t_base_task"
        taskCount = self.sqlite.getCount(sql)
        sql = "select * from t_base_node"
        nodeCount = self.sqlite.getCount(sql)
        if taskCount != 0 or nodeCount != 0:
            return False
        else:
            return True
