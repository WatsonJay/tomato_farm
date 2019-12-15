# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : loadConf.py
# @Soft    : tomato_farm
import configparser
import os
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from util.logger import logger

class config:
    def __init__(self, key=')_9-+klo@c4t$k$w'):
        log = logger()
        self.conflog = log.getlogger('conf')
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.dirs = os.path.abspath('.')+"/config/"
        self.fileName = "config.ini"

    # 读取配置文件
    def readConfig(self):
        config = configparser.ConfigParser()
        if not os.path.exists(self.dirs):
            os.makedirs(self.dirs)
        if not os.path.exists(self.dirs+self.fileName):
            f = open(self.dirs+self.fileName, 'w')
            f.close()
        try:
            config.read(self.dirs+self.fileName, encoding="utf-8")
            self.conflog.debug("配置文件已读取")
        except Exception as e:
            self.conflog.error(e)
        else:
            return config

    # 写入配置文件
    def writeConfig(self,config):
        try:
            config.write(open(self.dirs+self.fileName, "w", encoding='utf-8'))
            self.conflog.debug("配置文件已写入")
        except Exception as e:
            self.conflog.error(e)

    # 新增section
    def addSection(self, section):
        config = self.readConfig()
        if not config.has_section(section):  # 检查是否存在section
            config.add_section(section)
            self.conflog.debug("追加配置组："+section)
        self.writeConfig(config)

    # 新增option
    def addoption(self, section, option, word):
        config = self.readConfig()
        config.set(section, option, word)
        self.conflog.debug("在配置组：" + section + "下设置配置：" + option + "的值为：" + word)
        self.writeConfig(config)

    # 删除配置文件
    def delSection(self, section):
        config = self.readConfig()
        if config.has_section(section):
            config.remove_section(section)  # 整个section下的所有内容都将删除
            self.conflog.debug("删除配置组：" + section)
        self.writeConfig(config)

    #获得配置
    def getOption(self, section, option):
        config = self.readConfig()
        if config.has_section(section):
            word = config.get(section, option)
            self.conflog.debug("获取配置组：" + section + "下" + option + "的配置")
        else :
            word = ''
        return word

    # 获得配置
    def getSection(self):
        config = self.readConfig()
        word = config.sections()
        return word


    # 字符串切割成数组
    def splitword(self,word):
        if word != '':
            list = word.split(',')
        else:
            list = []
        return list

    # 数组转成字符串
    def split(self, list):
        if len(list) > 0:
            word = ','.join(list)
        else:
            word = ''
        return word

    #aes加密
    def encrypt(self,text):
        try:
            cryptor = AES.new(self.key,self.mode,self.key)
            length = 16
            count = len(text)
            if count < length:
                add = (length - count)
            elif count > length:
                add = (length - (count % length))
            text_new = (text + ('\0' * add)).encode('utf-8')
            self.ciphertext = cryptor.encrypt(text_new)
            return bytes.decode(b2a_hex(self.ciphertext), encoding='utf8')
        except Exception as e:
            self.conflog.error(e)
            return ''

    # aes解密
    def decrypt(self,text):
        try:
            cryptor = AES.new(self.key, self.mode, self.key)
            plain_text = bytes.decode(cryptor.decrypt(a2b_hex(bytes(text, encoding='utf8'))), encoding='utf8')
            return plain_text.rstrip('\0')
        except Exception as e:
            self.conflog.error(e)
            return ''


if __name__ == '__main__':
    con = config()
    con.readConfig()
    print(con.encrypt("False"))
