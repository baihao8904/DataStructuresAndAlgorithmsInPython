# -*- coding:utf-8 -*-
from ExerciseStackAndQueue.ListQuene import ListQuene
from ExerciseStackAndQueue.listStack import SStack

class BinTNode:
    def __init__(self,dat,left=None,right=None):
        self.data =dat
        self.left = left
        self.right = right

def count_BinNodes(T):
    if T is None:
        return 0
    else:
        return 1+count_BinNodes(T.left)+count_BinNodes(T.right)

def sum_BinNodes(T):
    if T is None:
        return 0
    else:
        return T.data+sum_BinNodes(T.left)+sum_BinNodes(T.right)

def preOrder(T,proc):
    if T is None:
        return
    proc(T.data)
    preOrder(T.left,proc)
    preOrder(T.right,proc)

def print_BinNode(T):
    if T is None:
        print("^" ,end='')
        return
    print("("+str(T.data),end="")
    print_BinNode(T.left)
    print_BinNode(T.right)
    print(")",end="")

#层次遍历
def levelOrder(T,proc):
    aQueue = ListQuene()
    aQueue.enquene(T)
    while not aQueue.is_empty():
        n = aQueue.dequeue()
        if n is None:
            continue
        aQueue.enquene(n.left)
        aQueue.enquene(n.right)
        proc(n.data)

#非递归的先根遍历
def preorder_nonrec(T,proc):
    aStack = SStack()
    while T is not None or not aStack.is_empty():
        while T is not None:
            proc(T.data)
            aStack.push(T.right)
            T = T.left
        T = aStack.pop()

#非递归的后根遍历算法
def postOrder_nonrec(T,proc):
    astack = SStack()
    while not astack.is_empty() or T is not None:
        while T is not None:
            astack.push(t)
            T = T.left if T.left is not None else T.right

        T = astack.pop()
        proc(T.data)
        if not astack.is_empty() and astack.top().left ==T:
            T = astack.top().right
        else:
            T = None

#有关二叉树的迭代器
def preorder_elements(T):
    aStack = SStack()
    while T is not None or not aStack.is_empty():
        while T is not None:
            aStack.push(T.right)
            yield T.data
            T = T.left
        T = aStack.pop()

if __name__ == '__main__':
    t = BinTNode(1,BinTNode(2,BinTNode(4),BinTNode(6)),BinTNode(3,BinTNode(8)))
    print(count_BinNodes(t))
    print(sum_BinNodes(t))
    preOrder(t,print)
    print_BinNode(t)
    print("层次遍历:")
    levelOrder(t,print)
    print("非递归的层次遍历：")
    preorder_nonrec(t,print)
    preorder_nonrec(t,lambda x:print(x,end=" "))
    print("\n")
    print("生成器")
    i = preorder_elements(t)
    for item in i:
        print(item,end=" ")