#!/usr/bin/python
#coding: utf-8

#import similarity2
from similarity2 import *
'''
#计算 所有的user的和 全部命中 除以 全部的元素总数
def recall(train,test,N):
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = getRecommendation(user,N)
        for item,pui in rank:
            if item in tu:
                hit += 1
        all += len(tu)
    return hit/(all*1.0)
def precision(train,test,N):
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = getRecommendation(user,N)
        for item,pui in rank:
            if item in tu:
                hit += 1
        all += N
    return hit/(all*1.0)

'''
def recallPre(train,test,N):
    hit = 0
    allRec = 0
    allPre = 0
    length = len(train)
    for user in train.keys():

        if int(user) > length: #算法有误 不好啊 用户不是从1 中间空白开始的啊
            continue

        if not test.has_key(user): #如果测试集中没有就跳过去
            continue
        tu = test[user]

        rank = getRecommendation(user,N)
        for item,pui in rank:
            if item in tu:
                hit += 1
        allRec += len(tu)
        allPre += N
    return hit/(allRec*1.0),hit/(allPre*1.0)

    '''给一个用户使用的
def recallPre(user,test,N):
    hit = 0
    allRec = 0
    allPre = 0

    tu = test[str(user)]

    rank = getRecommendation(user,N)
    for item,pui in rank:
        if item in tu:
            hit += 1
    allRec += len(tu)
    allPre += N
    return hit/(allRec*1.0),hit/(allPre*1.0)
'''

def getRecommendation(user,N):
    global train,weight
    rank = recommend(user,train,weight,8)
    rankN =(sorted(rank.items(), lambda x, y: cmp(x[1], y[1]),\
            reverse=True))[0:N]
    return rankN

    

if __name__ =='__main__':
    train = readFile(sys.argv[1])
    weight = similarity(train)
    test = readFile(sys.argv[2])

    #print recallPre(1000,test,20)
    print recallPre(train,test,8)
    #print getRecommendation(1,8)

    



