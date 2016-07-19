#!/usr/bin/python
# coding:  utf-8

import sys
import math

#读取文件 并按照用户进行归约
def readFile(name):
    print  "read file %s" % name
    fp=file(name)
    userIndex = dict()
    i = 0
    while True:
        line = fp.readline()
        if not line: break
        i += 1
        tmp = str(line).split('\t')
        #if 判断是否存在 不存在先定义list 这样让以后添加的都在同一level
        if not userIndex.has_key(tmp[0]):
            userIndex[tmp[0]] = []
        userIndex[tmp[0]].append(tmp[1])
    print "read file have done line number is %d" % i
    fp.close()
    return userIndex


#define the similarity function
def similarity(train):
    #定义二维list 存放权值
    w = [([0] * len(train)) for i in range(len(train))]
    
    for u in train.keys():
        for v in train.keys():
            if u==v:
                continue 
            uset =  set(train[u])
            vset =  set(train[v])
            uvset = uset & vset
            #需要判断 一下 len()函数 必须是存在的
            uw = int(u) - 1 
            vw = int(v) - 1
            if uvset:
                w[uw][vw]=len(uvset)
            w[uw][vw] /= math.sqrt(len(train[u])*len(train[v])*1.0)
    return w
        


text = readFile(sys.argv[1])
weight = similarity(text)
print weight










