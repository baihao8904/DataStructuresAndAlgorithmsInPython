# -*- coding:utf-8 -*-

class PrioQueueError(ValueError):
    pass

class PrioQueue():
    def __init__(self,elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in heap')
        return self._elems[0]

    #进堆
    def enQueue(self,e):
        self._elems.append(None)
        self.siftup(e,len(self._elems)-1)

    def siftup(self,e,last):
        elems = self._elems
        i,j = last,last//2
        while i>0 and e<elems[j]:
            elems[i] = elems[j]
            i,j = j,j//2
        elems[i] = e


    #出堆
    def deQueue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems)>0:
            self.siftdown(e,0,len(elems))
        return e

    def siftdown(self,e,begin,end):
        elems = self._elems
        i,j =begin,begin*2+1
        while j<end:
            if j+1 <end and elems[j]>elems[j+1]:
                j+=1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i,j = j,j*2+1
        elems[i] = e

    #堆的构建和初始化
    def buildheap(self):
        end = len(self._elems)-1
        # end//2的意思是最后的end//2个元素都是叶节点。将从他们之前的元素构建堆
        for i in range(end//2,-1,-1):
            self.siftdown(self._elems[i],i,end)

    def showheap(self):
        return self._elems


if __name__ == '__main__':
    test = PrioQueue([1,2,3,4,5,6,7,8])
    print(test.is_empty())
    test.enQueue(9)
    print(test.showheap())
    test.deQueue()
    print(test.showheap())