#Uses python3
import sys
def relax(dist,adj,cost):
    for v in range(len(adj)):
        for u in range(len(adj[v])):
            if dist[adj[v][u]]>dist[v]+cost[v][u]:
                dist[adj[v][u]] = dist[v] + cost[v][u]
                return 1
    return 0
def negative_cycle(adj,cost):
    if not (adj or cost):
        return 0
    vertexs = len(adj)
    dist = [vertexs+1] * vertexs
    dist[0] = 0
    for i in range(vertexs - 1):
        if not relax(dist,adj,cost):
            return 0
    return relax(dist,adj,cost)

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
    print(negative_cycle(adj, cost))
