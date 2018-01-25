#Uses python3

import sys

def acyclic(adj):
    visited=[]
    path=[]
    for u in range(len(adj)):
        if u not in visited and explore(u,adj,path,visited):
            return 1
    return 0


def explore(u,adj,path,visited):
    if u in path:
        return True
    #add the vertex u to visited and path list
    visited.append(u)
    path.append(u)
    #if we can go through from vertex u to vertex v, return True.
    for v in adj[u]:
        if explore(v,adj,path,visited):
            return True
    #remove current vertex u from path
    path.pop()
    return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
