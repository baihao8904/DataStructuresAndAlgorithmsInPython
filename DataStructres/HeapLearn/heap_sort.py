
def heap_sort(elems):
    def siftdown(elems,e,begin,end):
        i,j =begin,begin*2+1
        while j<end:
            if j+1 <end and elems[j]>elems[j+1]:
                j+=1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i,j = j,j*2+1
        elems[i] = e

    end = len(elems)
    for i in range(end//2,-1,-1):
        siftdown(elems,elems[i],i,end)
    print(elems)
    for i in range(end-1,0,-1):
        e= elems[i]
        #将排好序的元素放下i位置，对剩余的元素再进行排序
        elems[i] = elems[0]
        siftdown(elems,e,0,i)
    return elems


if __name__ == '__main__':
    test = [10,32,4,56,13,3,1,59,2,34]
    print(heap_sort(test))


