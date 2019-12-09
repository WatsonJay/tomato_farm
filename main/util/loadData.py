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

    #输出工具
    def out(self, outStr, *args):
        if (self.showsql):
            for var in args:
                if (var):
                    outStr = outStr + ", " + str(var)
            print("db. " + outStr)

    #执行sql或者查询列表 并提交
    def execute(self, sql, *args):
        args = self.turnArray(args)
        self.out(sql, args)

        cursor = self.conn.cursor()
        #sql占位符 填充args 可以是tuple(1, 2)(动态参数数组) 也可以是list[1, 2] list(tuple) tuple(list)
        res = cursor.execute(sql, args).fetchall()
        conn.commit()
        #self.close(conn)
        return res