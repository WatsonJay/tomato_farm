# -*- coding: utf-8 -*-
__author__ = 'Jaywatson'

import git
import os

class gitControl:
    def __init__(self):
        self.dirs = os.path.abspath("C:/Users/"+os.environ['USERNAME']+"/Documents/tomatoFarm/")
        self.dataPath = self.dirs + "/data/"
        if not os.path.exists(self.dataPath):
            os.makedirs(self.dataPath)
        self.url = "https://github.com/WatsonJay/tomato_farm_data.git"
        self.fileName = "config.ini"
        if not os.path.exists(self.dataPath+".git/"):
            git.Repo.clone_from(self.url,self.dataPath)
            print("cloned")
        else:
            self.repo = git.Repo(self.dataPath)
            head = self.repo.head
            self.repo.remote().pull()
            print("pulled")


if __name__ == '__main__':
    con = gitControl()
    print("readed")