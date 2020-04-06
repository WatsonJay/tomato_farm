# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : logger.py
# @Soft    : tomato_farm
import logging,os
import logging.config
import sys

import yaml

class logger:
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(sys.argv[0]))
        if not os.path.exists(self.path + "/log"):
            os.makedirs(self.path + "/log")
        with open(self.path+'/config/log.yaml', 'r', encoding='utf-8') as f:
            logConfig = yaml.safe_load(f.read())
            logConfig['handlers']['file']['filename'] = self.path+'/log/message.log'
            logging.config.dictConfig(logConfig)

    def getlogger(self,model):
        return logging.getLogger(model)