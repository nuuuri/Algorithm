# G[4] 메모리 175960 KB  시간 504 ms

import sys
from collections import deque

MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ice = []
ans = 0

def checkIce():
    queue = deque([ice[0]])
    visited = [[0] * M for _ in range(N)]
    visited[ice[0][0]][ice[0][1]] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()
        cnt += 1

        for dx, dy in MOVE:
            if 0 <= x+dx < N and 0 <= y+dy < M and arr[x+dx][y+dy] > 0 and not visited[x+dx][y+dy]:
                queue.append((x+dx, y+dy))
                visited[x+dx][y+dy] = 1

    return cnt == len(ice)

def meltIce():
    global ice
    ice = []
    temp = [a[:] for a in arr]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                continue

            for di, dj in MOVE:
                if 0 <= i+di < N and 0 <= j+dj < M and temp[i+di][j+dj] == 0 and arr[i][j] > 0:
                    arr[i][j] -= 1

            if arr[i][j] > 0:
                ice.append((i, j))

for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            ice.append((i, j))

while True:
    if not checkIce():
        print(ans)
        exit(0)     

    ans += 1
    meltIce()

    if not ice:
        print(0)
        exit(0)