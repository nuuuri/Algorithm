# G[3] 메모리 123584 KB  시간 784 ms

import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    x, y, c = map(int, sys.stdin.readline().split())
    graph[x-1].append((y-1, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [float("inf")] * N
    dist[start] = 0

    while q:
        cost, node = heapq.heappop(q)

        if dist[node] < cost:
            continue

        for next in graph[node]:
            if dist[next[0]] > dist[node] + next[1]:
                dist[next[0]] = dist[node] + next[1]
                heapq.heappush(q, (dist[node]+next[1], next[0]))

    return dist

dist = [dijkstra(i) for i in range(N)]
print(max([dist[x][X-1] + dist[X-1][x] for x in range(N)]))