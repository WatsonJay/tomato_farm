# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : loadData.py
# @Soft    : tomato_farm
import os
import sqlite3
import sys

from util.logger import logger


class sqlite:
    def __init__(self,filePath):
        self.file = filePath
        self.path = os.path.dirname(os.path.realpath(sys.argv[0]))
        log = logger()
        self.confsql = log.getlogger('conf')
        try:
            self.conn = sqlite3.connect(self.path+self.file, timeout=5)
            if (self.conn is None):
                raise Exception("dbfile :" + self.file + "is not found or connect error ! ")
            else:
                self.conn.row_factory = self.dict_factory
                self.confsql.info("connect successed")
        except Exception as e:
            self.confsql.error(e)
            raise e

    #以字典方式返回结果（可考虑替换为高度优化的sqlite3.Row类型）
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    # 查询列表
    def executeQuery(self, sql, *args):
        args = self.turnArray(args)
        self.out(sql, args)
        cursor = self.conn.cursor()
        res = cursor.execute(sql, args).fetchall()#大数据量时改造，确保内存
        return res

    #执行sql
    def execute(self,sql,*args):
        try:
            args = self.turnArray(args)
            self.out(sql, args)
            cursor = self.conn.cursor()
            res = cursor.execute(sql, args).fetchall()
            self.conn.commit()
            return res
        except Exception as e:
            self.confsql.error(e)
            raise e

    # 查询记录数量 自动附加count(*)
    def getCount(self, sql, *args):
        try:
            args = self.turnArray(args)
            sql = "select count(*) cc from ( " + sql + " ) "
            resString = self.resToString(sql, args)
            res = 0
            if (resString):
                res = int(resString)
        except Exception as e:
            self.confsql.error(e)
            raise e

    # 查询结果为单str
    def resToString(self,sql,*args):
        try:
            args = self.turnArray(args)
            self.out(sql, args)
            cursor = self.conn.cursor()
            listRes = cursor.execute(sql, args).fetchall()
            columnNames = [tuple[0] for tuple in cursor.description]
            res = ""
            if (listRes and len(listRes) >= 1):
                res = listRes[0][columnNames[0]]
            return res
        except Exception as e:
            self.confsql.error(e)
            raise e

        #关闭连接

    #关闭连接
    def close(self,conn=None):
        try:
            if (not conn is None):
                conn.close()
                self.conn=None
            self.confsql.info("database is closed")
        except Exception as e:
            self.confsql.error(e)
            self.conn = None

    #格式化参数
    def turnArray(self,args):
        try:
            # args ([1, 2, 3], ) list传入型 exe("select x x",[ 1, 2, 3]) len(args)=1 && type(args[0])=list
            # return [1, 2, 3]
            if (args and len(args) == 1 and (type(args[0]) is list)):
                res = args[0]
            # args (1, 2, 3) 直接调用型 exe("select x x", 1, 2, 3)
            # return [1, 2, 3] <- list(args)
            else:
                res = list(args)
            return res
        except Exception as e:
            self.confsql.error(e)
            raise e

    # 输出工具
    def out(self, outStr, *args):
        for var in args:
            if (var):
                outStr = outStr + ','  + str(var)
            self.confsql.debug('runed sql:'+outStr)