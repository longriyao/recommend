#coding:utf8
#find KthMax
from random import randint
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

def kIndex(ll,k):
    kInd = [0]*k
    kVaule = findKthMax(ll,k)
    i = 0
    kI = 0
    while i < len(ll):
        if ll[i] >= kVaule:
            kInd[kI] = i
            kI += 1
        i += 1
    return kInd


if __name__=='__main__':
    ll=[112,1,223,2,3,3,4,4,5,5,6,6,7,8,9]
    print ll
    print kIndex(ll,3)









