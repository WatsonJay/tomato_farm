# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 22:14
# @Author  : Jaywatson
# @File    : unlockWidgetImpl.py
# @Soft    : tomato_farm

import sys
from PyQt5.QtWidgets import QDialog
from UI.unlockDialog import Ui_unlockDialog
from UIImpls.noBorderImpl import noBorderImpl
from UIImpls.tipImpl import tipImpl
from util.loadConf import config

class unlockDialogImpl(QDialog, Ui_unlockDialog, noBorderImpl, tipImpl):
    # 初始化
    def __init__(self, parent=None):
        super(unlockDialogImpl, self).__init__(parent)
        self.setupUi(self)
        self.unlockPushButton.clicked.connect(self.unlock)
        self.passwordLineEdit.returnPressed.connect(self.unlock)

    def unlock(self):
        conf = config()
        if self.passwordLineEdit.text() == conf.decrypt(conf.getOption('system', 'password')):
            self.accept()
        else:
            self.Tips("密码错误,请重试")
        self.passwordLineEdit.setText("")