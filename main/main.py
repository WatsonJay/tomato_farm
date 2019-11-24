import os

from util.load_conf import config
from util.logger import logger

if __name__ == '__main__':
    if not os.path.exists("log"):
        os.makedirs("log")
    log = logger()
    mainlog = log.getlogger('root')
    mainlog.warning("xxxxxxxxxxxxxxxxxxxxx")
    con = config()
    con.readConfig()
    print("readed")