# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:43
# @Author  : Jaywatson
# @File    : gitControl.py
# @Soft    : tomato_farm
import git
import os

class gitControl:
    def __init__(self):
        #初始化参数配置，后期移至ini中加密存储
        self.dirs = os.path.abspath("C:/Users/"+os.environ['USERNAME']+"/Documents/tomatoFarm/")
        self.dataPath = self.dirs + "/data/"
        self.token = "325ef5bcf63841202a017f86b7d772f78c4073f4"
        self.account = "WatsonJay"
        self.password = "cywqoa19941121"
        self.fileName = "data.db"
        if not os.path.exists(self.dataPath):
            os.makedirs(self.dataPath)
        self.url = "https://" + self.account + ":" + self.password + "@github.com/WatsonJay/tomato_farm_data.git"
        #判断本地是否有git目录，存在既非初次运行
        if not os.path.exists(self.dataPath+".git/"):
            self.repo = git.Repo.clone_from(url=self.url,to_path=self.dataPath)
            print("cloned")
        else:
            self.repo = git.Repo(self.dataPath)
            print("finded")

    #提交
    def commitAndPush(self):
        print("pushed")

    #更新
    def pull(self):
        self.repo.remote().pull()
        print("pulled")

    #合并
    def merge(self):
        print("merge")

if __name__ == '__main__':
    con = gitControl()
    con.pull()
    print("readed")