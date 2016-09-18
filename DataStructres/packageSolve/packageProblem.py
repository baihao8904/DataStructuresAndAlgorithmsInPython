# -*- coding:utf-8 -*-
__author__ = 'lenovo'

def knap_rec(weight,wlist,n):
    if weight==0:
        return True
    if weight<0 or (weight>0 and n<1):
        return False
    if knap_rec(weight-wlist[n-1],wlist,n-1):
        print('item'+str(n)+':',wlist[n-1])
        return True
    if knap_rec(weight,wlist,n-1):
        return True
    else:
        return False



print(knap_rec(100,[1,2,3,4,5,6,7,8,20,30,40,50],12))