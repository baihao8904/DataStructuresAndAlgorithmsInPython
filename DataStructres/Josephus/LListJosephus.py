# -*- coding:utf-8 -*-

def josephus(n,k,m):
    people = [i for i in range(1,n+1)]

    i = k-1
    for personNum in range(n,0,-1):
        i = (i+m-1)% personNum
        print(people.pop(i),end=(',' if personNum>1 else '\n'))


if __name__ == '__main__':
    josephus(20,5,30)
