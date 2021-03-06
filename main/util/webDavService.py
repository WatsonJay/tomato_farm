# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 14:10
# @Author  : Jaywatson
# @File    : webDavService.py
# @Soft    : tomato_farm
import os
import sys

from webdav3.client import Client
from webdav3.exceptions import LocalResourceNotFound

from util.loadConf import config
from util.logger import logger


class webDavService:

    def __init__(self):
        self.conf = config()
        log = logger()
        self.path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.confwebdav = log.getlogger('webdav')
        self.options = {}
        self.client = None

    def loadBaseInfo(self):
        url = self.conf.decrypt(self.conf.getOption('webDav', 'url'))
        if url.endswith("/"):
            url = url[0:-1]
        self.options = {
            'webdav_hostname': url,
            'webdav_login': self.conf.decrypt(self.conf.getOption('webDav', 'username')),
            'webdav_password': self.conf.decrypt(self.conf.getOption('webDav', 'password')),
            # 'webdav_root': '/dav/',
            'disable_check': True,
        }
        self.client = Client(self.options)

    def creatDir(self):
        try:
            self.client.mkdir("tomato_db")
        except Exception as e:
            self.confwebdav.error(e)
            pass

    def clean(self):
        try:
            self.client.clean("tomato_db/tomato.db")
        except Exception as e:
            self.confwebdav.error(e)
            pass

    def upload(self, file):
        try:
            self.loadBaseInfo()
            self.creatDir()
            self.clean()
            self.client.upload(remote_path="tomato_db/tomato.db",
                               local_path=self.path + file)
        except Exception as e:
            self.confwebdav.error(e)
            pass

    def download(self, file):
        try:
            self.loadBaseInfo()
            self.client.download(remote_path="tomato_db/tomato.db",
                                 local_path=self.path + file)
        except Exception as e:
            self.confwebdav.error(e)
            pass

