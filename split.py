#!/usr/bin/python 
# coding: utf-8

import sys
import random



# data is dataset, N是总分数 k是测试集占总分数的第几分
def splitData(data,N,k):
    test = []
    train = []
    for line in data:
        if random.randint(0,N) == k:
            test.append(line)
        else:
            train.append(line)
    print "差分完数据集训练集 测试集的长度为 %d %d" % (len(train),len(test))
    return train,test
# 读取文件 
def readFile(name):
    fp = file(name,"r")
    text = []
    i = 0
    while True:
        line = fp.readline()
        if not line: break
        text.append(line)
        i = i+1
    fp.close()
    
    print "读完文件一共读了几行 %d" % i
    print "text长度 %d" % len(text)
    return text

def writeFile(train,test):
    fTrain = file("train.txt","w")
    fTest = file("test.txt","w")
    i = 0
    g = 0
    for line in train:
        i = i+1
        fTrain.write(line)

    for lineTest in test:
        #k=''.join([str(j) for j in line])

        g = g+1
        fTest.write(lineTest)
    
    print "写入文件完成 训练集 测试集写入行数为 %d %d" % (i,g)
    fTrain.close()
    fTest.close()

print "读取文件 %s" % sys.argv[1]
text = readFile(sys.argv[1]) 


train,test = splitData(text,8,2)
writeFile(train,test)













