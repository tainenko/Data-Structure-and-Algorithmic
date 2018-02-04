#Uses python3
import sys
import queue

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    vertices = len(adj)
    distance[s] = 0
    reachable[s] = 1
    queue = []
    visited = [False]*vertices

    for _ in range(vertices-1):
        for v in range(len(adj)):
            for u in range(len(adj[v])):
                if distance[adj[v][u]] > distance[v] + cost[v][u]:
                    distance[adj[v][u]] = distance[v] + cost[v][u]
                    reachable[adj[v][u]] = 1

    for v in range(vertices):
        for u in range(len(adj[v])):
            if distance[adj[v][u]] > distance[v] + cost[v][u]:
                if adj[v][u] not in queue:
                    queue.append(adj[v][u])

    while queue:
        u = queue.pop(0)
        visited[u] = True
        shortest[u] = 0
        for v in adj[u]:
            if not visited[v] and v not in queue:
                queue.append(v)

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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

