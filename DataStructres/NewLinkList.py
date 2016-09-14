#-*- coding:utf-8 -*-
#带尾节点引用的单链表
from random import randint

from LinkList import LList,LNode,LinkedListUnderFlow

class NewLList(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self,elem):
        if self._head is None:
            self._head = LNode(elem,self._head)
            self._rear = self._head
        else:
            self._head=LNode(elem,self._head)

    def append(self,elem):
        if self._head is None:
            self._head = LNode(elem,self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFlow
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

def test():
    mlist = NewLList()
    mlist.prepend(99)
    for i in range(20):
        mlist.append(randint(1, 20))
    print(mlist)
    mlist.printall()
    for x in mlist.filter(lambda y: y % 2 == 0):
        print(x, ' ', end='')

