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


class settingDialogImpl(QDialog, Ui_settingDialog, noBorderImpl, tipImpl):

    # 初始化
    def __init__(self, parent=None):
        super(settingDialogImpl, self).__init__(parent)
        self.setupUi(self)
        self.conf = config()
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
        self.gitNameEdit.setText(self.conf.getOption('github', 'username'))
        self.gitPasswordEdit.setText(self.conf.decrypt(self.conf.getOption('github', 'password')))
        self.gitProgramEdit.setText(self.conf.getOption('github', 'projectname'))

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
        self.conf.addoption('github', 'username', self.gitNameEdit.text())
        self.conf.addoption('github', 'password', self.conf.encrypt(self.gitPasswordEdit.text()))
        self.conf.addoption('github', 'projectname', self.gitProgramEdit.text())
        self.accept()