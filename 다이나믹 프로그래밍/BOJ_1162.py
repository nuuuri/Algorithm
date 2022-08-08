# G[1] 메모리 55744 KB  시간 1528 ms

import sys
import heapq

N, M, K = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y, d = map(int, sys.stdin.readline().split())
    graph[x].append((y, d))
    graph[y].append((x, d))

# dist[n][k] : n까지 가는 길에 k개 포장한 경우
def dijkstra(start):
    dist = [[float('inf') for _ in range(K + 1)] for _ in range(N + 1)]
    dist[start][0] = 0
    queue = []

    heapq.heappush(queue, (0, start, 0))

    while queue:
        current_dist, node, cnt = heapq.heappop(queue)
        
        if current_dist > dist[node][cnt]:
            continue

        for adj_node, next_dist in graph[node]:
            cost = current_dist + next_dist

            if cost < dist[adj_node][cnt]:
                dist[adj_node][cnt] = cost
                heapq.heappush(queue, (cost, adj_node, cnt))

            # 포장할 수 있는 경우 (current_dist + 0 < dist[adj_node][cnt+1])
            if cnt < K and current_dist < dist[adj_node][cnt+1]:
                dist[adj_node][cnt+1] = current_dist
                heapq.heappush(queue, (current_dist, adj_node, cnt+1))

    return min(dist[N])

print(dijkstra(1))