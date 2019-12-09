# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : loadData.py
# @Soft    : tomato_farm
import sqlite3
from util.logger import logger


class sqlite:
    def __init__(self,path):
        self.path = path
        log = logger()
        self.confsql = log.getlogger('conf')
        try:
            self.conn = sqlite3.connect(self.path, timeout=5)
            self.confsql.debug("连接成功")
        except Exception as e:
            self.confsql.error(e)
