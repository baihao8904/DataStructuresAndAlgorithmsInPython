# -*- coding:utf-8 -*-
__author__ = 'lenovo'

class StackUnserFlow(ValueError):
    pass

class SStack():
    def __init__(self):
        self._elems=[]

    def is_empty(self):
        return self._elems == []

    def top(self):
         if self._elems == []:
             raise StackUnserFlow('in listStack')
         return self._elems[-1]

    def push(self,elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems==[]:
            raise StackUnserFlow('in liststack pop')
        return self._elems.pop()


if __name__ == '__main__':
    S = SStack()
    S.push(5)
    S.push(6)
    print('top',S.top())
    while not S.is_empty():
        print(S.pop())