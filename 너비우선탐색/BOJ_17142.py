# G[4] 메모리 117872 KB  시간 332 ms

from itertools import combinations

N, M = map(int, input().split())
array = [[0 for _ in range(N)] for _ in range(N)]
vaccine_list = []
empty_room = 0
ans = -1

def findMaxTime(arr):
    time = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] not in ['-', '*'] and arr[i][j] > time:
                time = arr[i][j]

    return time

for i in range(N):
    for j, val in enumerate(map(int, input().split())):
        array[i][j] = val

        if val == 0:
            empty_room += 1
        elif val == 2:
            vaccine_list.append((i, j))

for vaccine in combinations(vaccine_list, M):
    arr = [[[-1, '-', '*'][array[i][j]] for j in range(N)] for i in range(N)]
    cnt = empty_room

    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = []

    for i,j in vaccine:
        arr[i][j] = 0
        visited[i][j] = True
        queue.append((i, j))

    while queue:
        if cnt == 0:
            break

        x, y = queue.pop(0)
        for dx, dy in [(-1,0), (0,-1), (1,0), (0,1)]:
            if 0 <= x+dx < N and 0 <= y+dy < N and visited[x+dx][y+dy] == False and arr[x+dx][y+dy] != '-':
                if arr[x+dx][y+dy] == -1:
                    cnt -= 1
                arr[x+dx][y+dy] = arr[x][y] + 1
                visited[x+dx][y+dy] = True
                queue.append((x+dx, y+dy))

    if cnt == 0:
        time = findMaxTime(arr)
        if ans == -1 or ans > time:
            ans = time

print(ans)