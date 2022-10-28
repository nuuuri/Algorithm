# G[1] 메모리 118604 KB  시간 328 ms

import sys
import heapq

N, P, K = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(P):
    x, y, cost = map(int, sys.stdin.readline().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, 1))
    dist = [float("inf")] * (N+1)
    dist[1] = 0

    while q:
        cost, node = heapq.heappop(q)

        if dist[node] < cost:
            continue

        for next in graph[node]:
            w = 1 if next[1] > x else 0

            if dist[next[0]] > dist[node] + w:
                dist[next[0]] = dist[node] + w
                heapq.heappush(q, (dist[node]+w, next[0]))

    return dist[N] <= K 

l, r = 0, 1000001
ans = -1

while (l <= r):
    mid = (l+r) // 2

    if (dijkstra(mid)):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)