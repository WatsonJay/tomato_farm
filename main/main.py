import os

from util.load_conf import config
from util.log.logger import logger

if __name__ == '__main__':
    log = logger()
    log.init()
    if not os.path.exists("./log"):
        os.makedirs("./log")
    log.getlogger('main')
    log.debug("hahhahahahahhahahahah")
    con = config()
    con.readConfig()
    print("readed")