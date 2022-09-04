# P[5] 메모리 145888 KB  시간 1460 ms

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
    def func(arr, x, y, d, temp):
        arr[x][y] = temp
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 오 아래 왼 위

        if temp == 1:
            return

        # x-1, y+1
        dx, dy = move[d]
        if 0 <= x+dx < R and 0 <= y+dy < C and (x+dx, y+dy) not in wall[x][y]:
            xx = x + dx + move[(d+1)%4][0]
            yy = y + dy + move[(d+1)%4][1]
            if 0 <= xx < R and 0 <= yy < C and (xx, yy) not in wall[x+dx][y+dy]:
                func(arr, xx, yy, d, temp-1)

        # x, y+1
        dx, dy = move[(d+1)%4]
        if  0 <= x+dx < R and 0 <= y+dy < C and (x+dx, y+dy) not in wall[x][y]:
            func(arr, x+dx, y+dy, d, temp-1)

        # x+1, y+1
        dx, dy = move[(d+2)%4]
        if 0 <= x+dx < R and 0 <= y+dy < C and (x+dx, y+dy) not in wall[x][y]:
            xx = x + dx + move[(d+1)%4][0]
            yy = y + dy + move[(d+1)%4][1]
            if 0 <= xx < R and 0 <= yy < C and (xx, yy) not in wall[x+dx][y+dy]:
                func(arr, xx, yy, d, temp-1)

    temp = [[0 for _ in range(C)] for _ in range(R)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    if d == 1:
        d = 2
    elif d == 2:
        d = 3
    elif d == 3:
        d = 1

    func(temp, x+dx[d], y+dy[d], d, 5)

    for i in range(R):
        for j in range(C):
            room[i][j] += temp[i][j]

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