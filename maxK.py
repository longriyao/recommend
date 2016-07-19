#!/usr/bin/python 
# coding: utf-8

'''
def maxK(num,k):
    kIndex =[0]*k
    num[1] = 100
    ki = 0  #记录循环
    while ki < k:
        max = num[0]    #记录最大值的
        index = 0       #记录最大值的index
        i = 0
        for j in num:
            if max >= j:
                i += 1
                continue
            max = j
            index = i
            i += 1
        kIndex[ki] = index
        ki += 1
            
    return kIndex
    '''
    
    

a = [12,3,4,34,12,1]
print maxK(a,3)











