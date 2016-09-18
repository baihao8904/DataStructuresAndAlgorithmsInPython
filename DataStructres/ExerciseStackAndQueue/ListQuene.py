# -*- coding:utf-8 -*-
__author__ = 'lenovo'

class QueneUnderFlow(ValueError):
    pass

class ListQuene():
    def __init__(self,init_len=8):
        self._len = init_len
        self._elems = [0]*init_len
        self._head = 0
        self._num =0

    def is_empty(self):
        return self._num==0

    def showLen(self):
        return self._len

    def peek(self):
        if self._num == 0:
            raise QueneUnderFlow
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueneUnderFlow
        e = self._elems[self._head]
        self._head = (self._head+1)%self._len
        self._num -=1
        return e

    def enquene(self,elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head+self._num)%self._len] = elem
        self._num +=1

    def __extend(self):
        oldLen = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(oldLen):
            new_elems[i]= self._elems[(self._head+i)%oldLen]
        self._elems,self._head = new_elems,0


if __name__ == '__main__':
    test = ListQuene()
    print(test.is_empty())
    test.enquene(5)
    test.enquene(6)
    print(test.showLen())
    for i in range(100,50,-5):
        test.enquene(i)
    print(test.showLen())
    print(test.is_empty())
    while not test.is_empty():
        print(test.dequeue(),end=' ')