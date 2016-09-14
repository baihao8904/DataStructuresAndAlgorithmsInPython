#-*- coding:utf-8 -*-
#循环单链表
from random import randint


class LinkedListUnderFlow:
    pass

class LNode:
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = None

class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self,elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    #尾端插入 相当于前端插入再将表首节点向后移
    def append(self,elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderFlow('in pop LClist')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem,end='')
            if p is self._rear:
                break
            else:
                print(',',end='')
            p = p.next
        print('')

    def filter(self,pred):
        p = self._rear.next
        while p is not self._rear:
            if pred(p.elem):
                yield p.elem
            p = p.next

def test():
    mlist = LCList()
    mlist.prepend(99)
    for i in range(20):
        mlist.append(randint(1,20))
    print(mlist)
    mlist.printall()
    for x in mlist.filter(lambda y:y%2==0):
        print(x, ' ',end='')

