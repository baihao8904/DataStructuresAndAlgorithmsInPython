# -*- coding:utf-8 -*-
from  ExerciseStackAndQueue.listStack import SStack

def DFS_graph(graph,v0):
    vnum = graph.vertex_num()
    visited = [0]*vnum
    visited[v0] =1
    DFS_seq = [v0,]
    st = SStack()
    st.push((0,graph.out_edges(v0)))
    while not st.is_empty():
        i,edges = st.pop()
        if i<len(edges):
            v,e = edges[i]
            st.push((i+1,edges))
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0,graph.out_edges(v)))
    print(DFS_seq)
    return DFS_seq