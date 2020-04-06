# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 22:02
# @Author  : Jaywatson
# @File    : winReg.py
# @Soft    : tomato_farm
import win32api
import win32con
import os
from util.loadConf import config


class winReg:
    def __init__(self):
        self.conf = config()
        self.systemName = self.conf.getOption('system', 'name')
        self.systemName = "tomato.exe"
        self.name = 'tomatoFarm'  # 要添加的项值名称
        self.path = '"' + os.path.abspath(self.systemName) + '" slient'  # 要添加的exe路径
        # 注册表项名
        self.KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        #self.KeyName = r"Volatile Environment"

    def addReg(self):
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, self.KeyName, 0, win32con.KEY_ALL_ACCESS)
            win32api.RegSetValueEx(key, self.name, 0, win32con.REG_SZ, self.path)
            win32api.RegCloseKey(key)
        except:
            raise OSError

    def checkName(self):
        try:
            key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, self.KeyName, 0, win32con.KEY_ALL_ACCESS)
            value = win32api.RegQueryValueEx(key, self.name)
            return True
        except:
            return False
        finally:
            win32api.RegCloseKey(key)

    def deleteReg(self):
        # 异常处理
        try:
            key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, self.KeyName, 0, win32con.KEY_ALL_ACCESS)
            win32api.RegDeleteValue(key, self.name)
            win32api.RegCloseKey(key)
        except Exception as e:
            pass

if __name__ == '__main__':
    reg = winReg()
    if reg.checkName():
        reg.deleteReg()
    reg.addReg()
    print(1)