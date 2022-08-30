# G[1] 메모리 30840 KB  시간 472 ms

import sys
input = sys.stdin.readline

MOVE = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
x, y = N//2, N//2
ans = 0

def snail(n):
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pos = []
    x, y = 0, -1
    d = 0

    while n > 0:
        for _ in range(n):
            x += move[d][0]
            y += move[d][1]
            pos.append((x, y))

        n -= 1
        d = (d+1) % 4

        for _ in range(n):
            x += move[d][0]
            y += move[d][1]
            pos.append((x, y))

        d = (d+1) % 4

    return pos

pos = list(reversed(snail(N)))[1:]
beads = [arr[i][j] for i, j in pos]

def moveBeads():
    for idx, (i, j) in enumerate(pos):
        if arr[i][j] == 0:
            beads[idx] = 0

    for _ in range(beads.count(0)):
        beads.remove(0)

def explodeBeads():
    global beads, ans

    while True:
        explosion = False
        idx, cnt = 1, 1

        while idx <= len(beads):
            if idx < len(beads) and beads[idx] == beads[idx-1]:
                cnt += 1
            else:
                if cnt >= 4:
                    explosion = True
                    ans += beads[idx-1] * cnt
                    beads = beads[:idx-cnt] + beads[idx:]
                    idx  = idx - cnt
                cnt = 1
            idx += 1

        if not explosion:
            break

def changeBeads():
    global arr, beads
    b, cnt = 0, 0
    for _ in range(len(beads)):
        bead = beads.pop(0)

        if b == 0:
            b = bead
            cnt = 1
            continue

        if bead == b:
            cnt += 1
        else:
            beads.append(cnt)
            beads.append(b)
            b = bead
            cnt = 1

    beads.append(cnt)
    beads.append(b)
    beads = beads[:N*N-1]

    for _ in range(N*N - 1 - len(beads)):
        beads.append(0)
    
    # arr 재설정
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for idx, (i, j) in enumerate(pos):
        arr[i][j] = beads[idx]

for _ in range(M):
    d, s = map(int, input().split())

    # 마법 시전
    for ss in range(1, s+1):
        dx = MOVE[d-1][0] * (ss)
        dy = MOVE[d-1][1] * (ss)

        if 0 <= x+dx < N and 0 <= y+dy < N:
            arr[x+dx][y+dy] = 0

    moveBeads()
    explodeBeads()
    changeBeads()

print(ans)