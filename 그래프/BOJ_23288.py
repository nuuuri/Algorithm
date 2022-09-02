# G[3] PyPy3 메모리 115364 KB  시간 192 ms / Python3 메모리 30840 KB  시간 600 ms

import sys
input = sys.stdin.readline

dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
MOVE = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y, d = 0, 0, 0
ans = 0

def rollTheDice(d):
    if d == 0:
        temp = dice[1][2]
        dice[1] = [dice[3][1], dice[1][0], dice[1][1]]
        dice[3][1] = temp
    elif d == 1:
        temp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = temp
    elif d == 2:
        temp = dice[1][0]
        dice[1] = [dice[1][1], dice[1][2], dice[3][1]]
        dice[3][1] = temp
    elif d == 3:
        temp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = temp

def bfs(i, j):
    queue = [(i, j)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[i][j] = True
    cnt = 0

    while queue:
        x, y = queue.pop(0)
        cnt += 1

        for dx, dy in MOVE:
            if 0 <= x+dx < N and 0 <= y+dy < M and not visited[x+dx][y+dy] and arr[x+dx][y+dy] == arr[x][y]:
                queue.append((x+dx, y+dy))
                visited[x+dx][y+dy] = True
    
    return cnt

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(K):
    dx, dy = MOVE[d]

    if 0 > x+dx or x+dx >= N or 0 > y+dy or y+dy >= M:
        d = (d+2) % 4 
        dx, dy = MOVE[d]

    rollTheDice(d)
    x += dx
    y += dy

    ans += arr[x][y] * bfs(x, y)

    if dice[3][1] > arr[x][y]:
        d = (d+1) % 4
    elif dice[3][1] < arr[x][y]:
        d = (d-1) % 4
    
print(ans)