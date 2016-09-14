# -*- coding:utf-8 -*-

def josephus_list(n,k,m):
    people = [i for i in range(1,n+1)]

    i=k-1
    for person in range(n):
        flag =0
        #一次循环出列一个
        while flag<m :
            if people[i]>0:
                flag+=1
            if flag==m:
                print(people[i],end='')
                people[i]=0
            i = (i+1)%n
        if person<n-1:
            print(',',end='')
        else:
            print('')

if __name__ == '__main__':
    josephus_list(20,5,30)

