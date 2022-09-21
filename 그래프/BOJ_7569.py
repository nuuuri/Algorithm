# G[5] 메모리 235480 KB  시간 640 ms

import sys
from collections import deque

MOVE = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
M, N, H = map(int, sys.stdin.readline().split())
arr = []
queue = deque([])

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if temp[j][k] == 1:
                queue.append((i, j, k, 1))
    arr.append(temp)

while queue:
    x, y, z, cnt = queue.popleft()

    for dx, dy, dz in MOVE:
        if 0 <= x+dx < H and 0 <= y+dy < N and 0 <= z+dz < M and arr[x+dx][y+dy][z+dz] == 0:
            arr[x+dx][y+dy][z+dz] = cnt + 1
            queue.append((x+dx, y+dy, z+dz, cnt+1))

day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                print(-1)
                exit(0)

            if arr[i][j][k] > day:
                day = arr[i][j][k]

print(day - 1)