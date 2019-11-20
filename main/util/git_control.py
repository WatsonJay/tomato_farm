# -*- coding: utf-8 -*-
__author__ = 'Jaywatson'

import git
import os

class gitControl:
    def __init__(self):
        self.dirs = os.path.abspath("C:/Users/"+os.environ['USERNAME']+"/Documents/tomatoFarm/")
        self.dataPath = self.dirs + "/data/"
        self.token = "325ef5bcf63841202a017f86b7d772f78c4073f4"
        if not os.path.exists(self.dataPath):
            os.makedirs(self.dataPath)
        self.url = "https://" + self.token + "@github.com/WatsonJay/tomato_farm_data.git"
        self.fileName = "data.acc"
        if not os.path.exists(self.dataPath+".git/"):
            self.repo = git.Repo.clone_from(url=self.url,to_path=self.dataPath)
            print("cloned")
        else:
            self.repo = git.Repo(self.dataPath)
            print("finded")

    def commitAndPush(self):
        print("pushed")

    def pull(self):
        print("pulled")

    def merge(self):
        print("merge")

if __name__ == '__main__':
    con = gitControl()
    print("readed")