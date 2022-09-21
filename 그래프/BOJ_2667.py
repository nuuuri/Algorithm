# S[1] 메모리 114328 KB  시간 112 ms

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
complex = []

def bfs(i, j):
    queue = [(i, j)]
    visited[i][j] = True
    cnt = 0

    while queue:
        x, y = queue.pop(0)
        cnt += 1

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x+dx < N and 0 <= y+dy < N and arr[x+dx][y+dy] == '1' and not visited[x+dx][y+dy]:
                queue.append((x+dx, y+dy))
                visited[x+dx][y+dy] = True

    complex.append(cnt)

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            bfs(i, j)

print(len(complex))
for c in sorted(complex):
    print(c)
