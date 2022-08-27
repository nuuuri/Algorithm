# G[5] 메모리 116096 KB  시간 228 ms

import sys
input = sys.stdin.readline

MOVE = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for _ in range(M):
    d, s, = map(int, input().split())
    l = len(cloud)
    visited = [[False for _ in range(N)] for _ in range(N)]

    # 구름 이동
    di, dj = MOVE[d-1][0]*s, MOVE[d-1][1]*s
    for _ in range(l):
        i, j = cloud.pop(0)
        x, y = (i+di)%N, (j+dj)%N

        cloud.append((x, y))
        arr[x][y] += 1
        visited[x][y] = True

    # 물복사버그
    for i, j in cloud:
        cnt = 0

        for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if 0 <= i+di < N and 0 <= j+dj < N and arr[i+di][j+dj] > 0:
                cnt += 1

        arr[i][j] += cnt

    new_cloud = []    
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not visited[i][j]:
                arr[i][j] -= 2
                new_cloud.append((i, j))

    cloud = new_cloud

print(sum(sum(a) for a in arr))