# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 14:10
# @Author  : Jaywatson
# @File    : webDavService.py
# @Soft    : tomato_farm

from webdav3.client import Client
from webdav3.exceptions import LocalResourceNotFound

from util.loadConf import config


class webDavService:

    def __init__(self):
        self.conf = config()
        self.options = {}
        self.client = None

    def loadBaseInfo(self):
        self.options = {
            'webdav_hostname': self.conf.decrypt(self.conf.getOption('webDav', 'url')),
            'webdav_login':    self.conf.decrypt(self.conf.getOption('webDav', 'username')),
            'webdav_password': self.conf.decrypt(self.conf.getOption('webDav', 'password'))
        }
        self.client = Client(self.options)

    def creatDir(self):
        try:
            if not self.client.check("tomato_db"):
                self.client.mkdir("tomato_db")
        except Exception as e:
            pass

    def upload(self):
        print(1)


if __name__ == '__main__':
    webDav = webDavService()
    webDav.creatDir()
