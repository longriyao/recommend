#!/usr/bin/python
# coding:  utf-8

import sys
import math
from random import randint
'''上一个算法 很多计算没有必要 计算了很多没有共同项之间的相似 没有必要
算法描述:
    先建立 物品到用户的倒序表对于每个物品都保存对该物品产生过行为的用户
列表。令稀疏矩阵C[u][v]= N ( u ) 交 N ( v ) 。那么,假设用户u和用户v同时属
于倒排表中K个物品对 应的用户列表,就有C[u][v]=K。从而,可以扫描倒排表中每个
物品对应的用户列表,将用户列 表中的两两用户对应的C[u][v]加1,最终就可以得
到所有用户之间不为0的C[u][v]'''

#读取文件 并按照用户进行归约 返回 user item的字典 
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


def similarity(train):
    #定义二维list 存放权值
    w = [([0] * len(train)) for i in range(len(train))]

    #build inverse table for item_users
    itemUsers = dict()
    for u,items in train.items():
        for item in items:
            #这里没有考虑重复的因素
            if not itemUsers.has_key(item):
                itemUsers[item] = []
            itemUsers[item].append(u)


    #calculate co-rated items between users
    #userNum = dict()         #记录每个用户有多少个相关用户
    userNum = [0]*len(train)
    for item,users in itemUsers.items():
        for user in users:
            userInt = int(user) -1
            userNum[userInt] += 1
            '''使用字典的时候使用
            if not userNum.has_key(user):
                userNum[user] = 0
            userNum[user] += 1 
            '''
            for v in users:
                if user == v:
                    continue
                uw = int(user) - 1 
                vw = int(v) - 1
                w[uw][vw] += 1

    #calculate finial similarity matrix
    wi = -1
    for u in w:
        wi += 1
        wj = -1 #重新初始化
        for v in u:
            wj += 1
            if v == 0:
                continue
            w[wi][wj] = v / math.sqrt(userNum[wi]*userNum[wj])
    return w

#定义 找到第k大的函数
def findKthMax(l,k):
    if k>len(l):
        return
    key=randint(0,len(l)-1)
    keyv=l[key]
    sl=[i for i in l[:key]+l[key+1:] if i<keyv]
    bl=[i for i in l[:key]+l[key+1:] if i>=keyv]
    if len(bl)==k-1:
        return keyv
    elif len(bl)>=k:
        return findKthMax(bl,k)
    else:
        return findKthMax(sl,k-len(bl)-1)

    th=findKthMax(ll,3)

#返回最大k值的index
def kIndex(ll,k):
    kInd = [0]*k #记录返回的数据
    kVaule = findKthMax(ll,k)  
    i = 0
    kI = 0
    while (i < len(ll) and(kI < k)): #可能有些是 kvalue是重复的
        if ll[i] >= kVaule:
            kInd[kI] = i
            kI += 1
        i += 1
    return kInd

    #定义推荐算法
def recommend(user,train,weight,k): #user是指的一个用户 求他的推荐物品
    rank = dict()
    interacted_items = train[str(user)]

    wUser = int(user) - 1
    userWei = weight[wUser] #user和其他用户的权重
    uKIndex = kIndex(userWei,k) #得到user最大k值的索引
    for i in uKIndex:
        i += 1          #索引和用户对应关系 要加1
        tmpTrain = train[str(i)]
        i -= 1          #下面要用到取数
        for item in tmpTrain:
            if item in interacted_items: #如果在的话表示user已经看过了
                continue
            if not rank.has_key(item):
                rank[item] = userWei[i]
            rank[item] += userWei[i]
            #rank[i] += wuv*rvi  rvi使用的是单一行为的隐反馈数据 所以为1
            # 可以为 rating
    return rank

if __name__ == "__main__":

    train = readFile(sys.argv[1])
    weight = similarity(train)
    rank = recommend(1,train,weight,8)
'''     推荐前几个
rand8 =sorted(rank.items(), lambda x, y: cmp(x[1], y[1]),reverse=True):[0:8]
'''












