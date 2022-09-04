# P[5] 메모리 121948 KB  시간 672 ms

import sys, copy
input = sys.stdin.readline

R, C, K = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
wall = [[[] for _ in range(C)] for _ in range(R)]
heater = []
pos = [] # 조사해야 하는 좌표
ans = 0

for x in range(R):
    for y in range(C):
        if 0 < room[x][y] < 5:
            heater.append((x, y, room[x][y]-1))
            room[x][y] = 0
        elif room[x][y] == 5:
            pos.append((x, y))
            room[x][y] = 0

for _ in range(W):
    x, y, t = map(int, input().split())
    if t == 0:
        wall[x-1][y-1].append((x-2, y-1))
        wall[x-2][y-1].append((x-1, y-1))
    else:
        wall[x-1][y-1].append((x-1, y))
        wall[x-1][y].append((x-1, y-1))

def turnOnHeater(x, y, d):
    MOVE = [[(-1,0),(0,1),(1,0)], [(-1,0),(0,-1),(1,0)], [(0,1),(-1,0),(0,-1)], [(0,1),(1,0),(0,-1)]]
    move = MOVE[d]
    queue = [(x+move[1][0], y+move[1][1], 5)]
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[x+move[1][0]][y+move[1][1]] = True

    while queue:
        x, y, temp = queue.pop(0)
        room[x][y] += temp

        if temp == 1:
            continue

        # 대각선
        for d in [0, 2]:
            dx, dy = move[d]
            dxx, dyy = move[1]
            if 0 <= x+dx < R and 0 <= y+dy < C and (x+dx, y+dy) not in wall[x][y]:
                if 0 <= x+dx+dxx < R and 0 <= y+dy+dyy < C and (x+dx+dxx, y+dy+dyy) not in wall[x+dx][y+dy]:
                    if not visited[x+dx+dxx][y+dy+dyy]:
                        queue.append((x+dx+dxx, y+dy+dyy, temp-1))
                        visited[x+dx+dxx][y+dy+dyy] = True
        
        # 옆
        dx, dy = move[1]
        if 0 <= x+dx < R and 0 <= y+dy < C and (x+dx, y+dy) not in wall[x][y] and not visited[x+dx][y+dy]:
            queue.append((x+dx, y+dy, temp-1))
            visited[x+dx][y+dy] = True

while ans <= 100:
    for x, y, d in heater:
        turnOnHeater(x, y, d)

    _room = copy.deepcopy(room)
    for i in range(R):
        for j in range(C):
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if 0 <= i+di < R and 0 <= j+dj < C and _room[i][j] > _room[i+di][j+dj] and (i+di, j+dj) not in wall[i][j]:
                    temp = (_room[i][j] - _room[i+di][j+dj])//4
                    room[i][j] -= temp
                    room[i+di][j+dj] += temp

    for i in range(R):
        for j in range(C):
            if (i == 0 or i == R-1 or j == 0 or j == C-1) and room[i][j] > 0:
                room[i][j] -= 1 

    ans += 1

    isValid = True
    for x, y in pos:
        if room[x][y] < K:
            isValid = False
            break

    if isValid:
        break

print(ans)