#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    #intialize the startting condiction, dst==0 and visited list is empty
    q=queue.Queue()
    dst=[None]*len(adj)

    #put the vertex s in the queue list
    q.put(s)
    dst[s]=0

    #if there are edges, the queue would not be empty
    while not q.empty():
        #get the vertex from the queue , and add it to the visited list
        v=q.get()

        #explore the adjecent vertex which is not visited, and add the distance by 1
        for u in adj[v]:
            if t==u:
                return dst[v] + 1
            if dst[u] is None:
                q.put(u)
                dst[u]=dst[v]+1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
