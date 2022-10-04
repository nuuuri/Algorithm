# G[2] 메모리 115968 KB  시간 172 ms

import sys

N, K = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]
board = [[[] for _ in range(N)] for _ in range(N)]
chessmen = []

def isNextBlue(x, y):
    return 0 > x or x >= N or 0 > y or y >= N or MAP[x][y] == 2

def turn(d):
    return d-1 if d%2 else d+1

def sol():
    cnt = 1

    while cnt <= 1000:
        for idx in range(K):
            x, y = chessmen[idx]

            if (x, y) == (-1, -1):
                continue

            c, d = board[x][y][0]
            dx, dy = DIR[d]

            if isNextBlue(x+dx, y+dy):
                d = turn(d)
                dx, dy = DIR[d]
                board[x][y][0] = c, d

                if isNextBlue(x+dx, y+dy):
                    continue

            if MAP[x+dx][y+dy] == 1:
                board[x][y] = board[x][y][::-1]

            board[x+dx][y+dy].extend(board[x][y])
            board[x][y] = []

            if len(board[x+dx][y+dy]) >= 4:
                return cnt

            for i in range(len(board[x+dx][y+dy])):
                c, d = board[x+dx][y+dy][i]

                if i == 0:
                    chessmen[c] = (x+dx, y+dy)
                else:
                    chessmen[c] = (-1, -1)

        cnt += 1

    return -1 if cnt > 1000 else cnt

for idx in range(K):
    x, y, d = map(int, sys.stdin.readline().split())
    board[x-1][y-1].append((idx, d-1))
    chessmen.append((x-1, y-1))

print(sol())