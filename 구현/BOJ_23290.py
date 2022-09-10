# G[1] 메모리 116588 KB  시간 196 ms

import sys

MOVE = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
M, S = map(int, sys.stdin.readline().split())
fish = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]

for _ in range(M):
    x, y, d = map(int, sys.stdin.readline().split())
    fish[x-1][y-1][d-1] += 1

shark = tuple(map(lambda x: int(x)-1, sys.stdin.readline().split()))

for _ in range(S):
    # 물고기 이동
    new_fish = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4): 
            for d in range(8):
                if fish[i][j][d] == 0:
                    continue

                cnt = fish[i][j][d]
                di, dj = MOVE[d]
                isMove = False

                for _ in range(8):
                    if 0 <= i+di < 4 and 0 <= j+dj < 4 and smell[i+di][j+dj] == 0 and (i+di, j+dj) != shark:
                        isMove = True
                        break

                    d = (d-1)%8
                    di, dj = MOVE[d]

                if isMove:
                    new_fish[i+di][j+dj][d] += cnt
                else:
                    new_fish[i][j][d] += cnt

    # 상어 이동
    shark_move_priority = [2, 0, 6, 4]
    visited = [[False for _ in range(4)] for _ in range(4)]
    path = []
    cost = -1
    def moveShark(x, y, t, c, p):
        global path, cost

        if t == 3:
            if c > cost:
                cost = c
                path = p

            return

        for m in shark_move_priority:
            dx, dy = MOVE[m]

            if 0 <= x+dx < 4 and 0 <= y+dy < 4:
                if visited[x+dx][y+dy]:
                    moveShark(x+dx, y+dy, t+1, c, p[:]+[m])
                else:
                    visited[x+dx][y+dy] = True
                    moveShark(x+dx, y+dy, t+1, c+sum(new_fish[x+dx][y+dy]), p[:]+[m])
                    visited[x+dx][y+dy] = False
        
    moveShark(shark[0], shark[1], 0, 0, [])

    # 물고기 제외
    for p in path:
        di, dj = MOVE[p]
        shark = shark[0]+di, shark[1]+dj

        if sum(new_fish[shark[0]][shark[1]]) > 0:
            new_fish[shark[0]][shark[1]] = [0 for _ in range(8)]
            smell[shark[0]][shark[1]] = 3

    # 냄새 사람짐 & 물고기 복제
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1

            for d in range(8):
                fish[i][j][d] += new_fish[i][j][d]

ans = 0
for i in range(4):
    for j in range(4):
        ans += sum(fish[i][j])
print(ans)