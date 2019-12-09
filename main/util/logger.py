# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : logger.py
# @Soft    : tomato_farm
import logging,os
import logging.config
import yaml

class logger:
    def __init__(self):
        with open('./config/log.yaml', 'r', encoding='utf-8') as f:
            logConfig = yaml.safe_load(f.read())
            logging.config.dictConfig(logConfig)

    def getlogger(self,model):
        return logging.getLogger(model)