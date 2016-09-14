# -*- coding:utf-8 -*-
#双链表
from random import randint

from LinkList import LNode,LinkedListUnderFlow
from NewLinkList import NewLList

class DLNode(LNode):
    def __init__(self,elem,prev_=None,next_=None):
        LNode.__init__(self,elem,next_)
        self.prev = prev_

class DLList(NewLList):
    def __init__(self):
        NewLList.__init__(self)

    def prepend(self,elem):
        p = DLNode(elem,None,self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self,elem):
        p = DLNode(elem,self._rear,None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderFlow('dList pop')
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFlow('dList PopLast')
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e


def test1():
    mlist = DLList()
    mlist.prepend(90)
    mlist.printall()
    for i in range(20):
        mlist.append(randint(1, 20))
    #print(mlist)
    mlist.printall()
    for x in mlist.filter(lambda y: y % 2 == 0):
        pass
       # print(x, ' ', end='')

test1()
