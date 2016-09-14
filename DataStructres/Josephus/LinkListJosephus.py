# -*- coding:utf-8 -*-
from  LCList import LNode,LCList
#基于循环单链表的解
#找到需要弹出的元素的下一项
class Josephus(LCList):
    def turn(self,m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self,n,k,m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop(),end=(',' if not self.is_empty() else "\n"))


if __name__ == '__main__':
    test = Josephus(20,5,30)
