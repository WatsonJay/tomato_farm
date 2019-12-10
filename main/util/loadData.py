# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : loadData.py
# @Soft    : tomato_farm
import sqlite3
from util.logger import logger


class sqlite:
    def __init__(self,filePath):
        self.file = filePath
        log = logger()
        self.confsql = log.getlogger('conf')
        try:
            self.conn = sqlite3.connect(self.file, timeout=5)
            if (self.conn is None):
                raise Exception("dbfile :" + self.file + "is not found or connect error ! ")
            else:
                self.conn.row_factory = self.dict_factory
                self.confsql.info("connect successed")
        except Exception as e:
            self.confsql.error(e)

    #以字典方式返回结果（可考虑替换为高度优化的sqlite3.Row类型）
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    # 查询列表
    def executeQuery(self, sql, *args):
        args = self.turnArray(args)
        self.out(sql,args)
        cursor = self.conn.cursor()
        res = cursor.execute(sql, args).fetchall()#大数据量时改造，确保内存
        return res

        #关闭连接
    def close(self,conn=None):
        if (not conn is None):
            conn.close()
            self.conn=None
        self.confsql.info("database is closed")

    # 输出工具
    def out(self, outStr, *args):
        for var in args:
            if (var):
                if ("'%s'" in outStr):
                    outStr = outStr.replace("'%s'",var,1)
                if ("?" in outStr):
                    outStr = outStr.replace("?",var,1)
            self.confsql.debug('runed sql:'+outStr)