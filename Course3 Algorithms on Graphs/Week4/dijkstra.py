#Uses python3

import sys
from queue import PriorityQueue
'''
Relax((u, v) ∈ E)
  if dist[v] > dist[u] + w(u, v):
    dist[v] ← dist[u] + w(u, v)
    prev[v] ← u
'''
'''Pseudocode
Dijkstra(G, S)
for all u ∈ V:
dist[u] ← ∞, prev[u] ← nil
dist[S] ← 0
H ← MakeQueue(V) {dist-values as keys}
while H is not empty:
u ← ExtractMin(H)
 for all (u, v) ∈ E:
if dist[v] > dist[u] + w(u, v):
dist[v] ← dist[u] + w(u, v)
prev[v] ← u
ChangePriority(H, v, dist[v]) '''

def distance(adj, cost, s, t):
    #write your code here
    dist=[float('inf')]*len(adj)
    dist[s] = 0
    q = PriorityQueue()
    q.put([dist[s],s])
    while not q.empty():
        vertex = q.get()
        u=vertex[1]
        #using index i to find the weight of vertex v in the  "cost list"
        for v in adj[u]:
            i=adj[u].index(v)
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                q.put((dist[v],v))
    if dist[t] == float('inf'):
        return -1
    return dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
