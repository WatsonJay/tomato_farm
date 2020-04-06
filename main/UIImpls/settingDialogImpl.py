# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 10:47
# @Author  : Jaywatson
# @File    : settingDialogImpl.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import QDialog

from UI.settingDialog import Ui_settingDialog
from UIImpls.noBorderImpl import noBorderImpl
from UIImpls.tipImpl import tipImpl
from util.loadConf import config
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

    #加载配置i
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
        self.gitNameEdit.setText(self.conf.getOption('github', 'username'))
        self.gitPasswordEdit.setText(self.conf.decrypt(self.conf.getOption('github', 'password')))
        self.gitProgramEdit.setText(self.conf.getOption('github', 'projectname'))
        try:
            if not self.autoOnButton.isChecked():
                self.conf.addoption('system', 'autoOn', "False")
        except:
            pass
        if self.conf.getOption('system', 'autoOn') == "True":
            self.autoOnButton.setChecked(True)
        else:
            self.autoOffButton.setChecked(True)

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
        self.conf.addoption('github', 'username', self.gitNameEdit.text())
        self.conf.addoption('github', 'password', self.conf.encrypt(self.gitPasswordEdit.text()))
        self.conf.addoption('github', 'projectname', self.gitProgramEdit.text())
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
        self.accept()

