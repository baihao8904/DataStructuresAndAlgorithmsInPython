# -*- coding:utf-8 -*-

from ExerciseGraph import ListGraph
from ExerciseGraph import dfsExercise

class GraphAL(ListGraph.Graph):
    def __init__(self,mat=[],unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x)!= vnum:
                raise ListGraph.GraphError
        self._mat = [ListGraph.Graph._out_edges(mat[i],unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum +=1
        return self._vnum -1

    def add_edge(self,vi,vj,val=1):
        if self._vnum == 0 :
            raise ListGraph.GraphError
        if self._invalid(vi) or self._invalid(vj):
            raise ListGraph.GraphError
        row = self._mat[vi]
        i = 0
        while i <len(row):
            if row[i][0] == vj:
                self._mat[vi][i] =(vj,val)
                return
            if row[i][0]>vj:
                break
            i+=1
        self._mat[vi].insert(i,(vj,val))

    def get_edge(self,vi,vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ListGraph.GraphError
        for i,val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edges(self,vi):
        if self._invalid(vi):
            raise ListGraph.GraphError
        return self._mat[vi]

if __name__ == '__main__':
    mat=[[1,0,1],[0,1,0],[1,0,1]]
    test =GraphAL(mat)
    print(test)
    print(test.get_edge(1,2))
    print(test.out_edges(1))
    print(dfsExercise.DFS_graph(test,2))
