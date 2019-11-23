# -*- coding: utf-8 -*-
__author__ = 'Jaywatson'

import logging,os
import logging.config

class logger:
    def init(self):
        logging.config.fileConfig('./config/log.conf')

    def getlogger(self,model):
        return logging.getLogger(model)

    def debug(self,message):
        logging.debug(message)

    def info(self,message):
        logging.info(message)

    def warning(self,message):
        logging.warning(message)

    def critical(self,message):
        logging.critical(message)