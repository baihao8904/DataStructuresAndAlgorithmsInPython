# -*- coding:utf-8 -*-
#单链表的实现
class LinkedListUnderFlow(ValueError):
    pass

class LNode:
    def __init__(self,elem,next_ = None):
        self.elem =elem
        self.next = next_

class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self,elem):
        self._head = LNode(elem,self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderFlow("in pop")
        e = self._head.elem
        if __name__ == '__main__':
            self._head = self._head.next
        return e

    def append(self,elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFlow('in poplast')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self,pred):
        p = self._head
        while p.next is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def filter(self,pred):
        p = self._head.next
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem,end='')
            if p.next is not None:
                print(',',end='')
            p = p.next
        print('')

    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return

        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p

def useLnode():
    head = LNode(1)
    p = head
    for i in range(2,11):
        p.next = LNode(i)
        p = p.next

    p = head
    while p is not None:
        print(p.elem)
        p = p.next

def useLLink():
    mlist1 =LList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(20,10,-1):
        mlist1.append(i)
    mlist1.pop()
    mlist1.pop_last()
    mlist1.printall()
    mlist1.sort()
    mlist1.printall()


if __name__ == '__main__':
    useLLink()