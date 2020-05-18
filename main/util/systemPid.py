# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 17:42
# @Author  : Jaywatson
# @File    : systemPid.py
# @Soft    : tomato_farm

import os
import sys
import psutil

class systemPid:
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.file = os.path.dirname(os.path.realpath(sys.argv[0])) + "/config/pid"
    #写入pid
    def write_pid(self):
        pid = os.getpid()

        fp = open(self.file, "w")
        fp.write(str(pid))
        fp.close()

    #读取pid
    def read_pid(self):
        try:
            if os.path.exists(self.file):
                fp = open(self.file, 'r')
                pid = fp.read()
                fp.close()
                return pid
            else:
                return "0"
        except Exception as e:
            return "0"

    #检测pid
    def check_pid(self):
        pid = self.read_pid()
        try:
            pid = int(pid)
        except Exception:
            pid = 0
        if pid != 0:
            running_pid = psutil.pids()
            if pid in running_pid:
                return False
            else:
                return True
        else:
            return True