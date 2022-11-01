# G[4] 메모리 129992 KB  시간 248 ms

import sys
from collections import deque

N, K, R = map(int, sys.stdin.readline().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
road = [[[] for _ in range(N)] for _ in range(N)]
cow = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
group = []

def bfs(start):
    q = deque([(start)])
    visited[start[0]][start[1]] = 1
    temp = []

    if cow[start[0]][start[1]] == 1:
        temp.append(start)

    while q:
        x, y = q.popleft()

        for xx, yy in graph[x][y]:
            if not visited[xx][yy]:
                visited[xx][yy] = 1
                q.append((xx, yy))

                if cow[xx][yy] == 1:
                    temp.append((xx, yy))
            
    group.append(len(temp))

def count(list):
    temp = [[0 if i==j else list[i]*list[j] for j in range(len(list))] for i in range(len(list))]

    return sum([sum(t) for t in temp]) // 2

for _ in range(R):
    x, y, xx, yy = map(int, sys.stdin.readline().split())
    road[x-1][y-1].append((xx-1, yy-1))
    road[xx-1][yy-1].append((x-1, y-1))

for i in range(N):
    for j in range(N):
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 > x or x >= N or 0 > y or y >= N or (x, y) in road[i][j]:
                continue

            graph[i][j].append((x, y))

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    cow[x-1][y-1] = 1

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs((i, j))

print(count(group))