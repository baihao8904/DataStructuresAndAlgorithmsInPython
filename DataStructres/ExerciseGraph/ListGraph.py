# -*- coding:utf-8 -*-

class GraphError(ValueError):
    pass

class Graph:
    def __init__(self,mat,unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x)!= vnum:
                raise GraphError
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        return self._vnum

    def _invalid(self,v):
        return 0>v or v>self._vnum

    def add_vertex(self):
        raise ValueError

    def add_edge(self,vi,vj,val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError
        self._mat[vi][vj] = val

    def get_edge(self,vi,vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError
        return self._mat[vi][vj]

    def out_edges(self,vi):
        if self._invalid(vi):
            raise GraphError
        return self._out_edges(self._mat[vi],self._unconn)

    @staticmethod
    def _out_edges(row,unconn):
        edges=[]
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i,row[i]))
        return edges

    def __str__(self):
        return "[\n" + ",\n".join(map(str,self._mat))+"\n]"+"\nUnconned:"+str(self._unconn)

if __name__ == '__main__':
    mat=[[1,2,3],[1,2,3],[4,5,6]]
    test =Graph(mat)
    print(test)