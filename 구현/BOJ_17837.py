# G[2] 메모리 117900 KB  시간 276 ms

N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]
board = [[[] for _ in range(N)] for _ in range(N)]
cnt = 0

def turn(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

def findIndex(num):
    for i in range(N):
        for j in range(N):
            for k, item in enumerate(board[i][j]):
                if item[0] == num:
                    return (i, j, k)

def move(i, j, k):
    chessman = board[i][j][k:]
    board[i][j] = board[i][j][:k]

    di, dj = DIR[chessman[0][1]]
    if i+di < 0 or i+di >= N or j+dj < 0 or j+dj >= N or MAP[i+di][j+dj] == 2:
        chessman[0] = (chessman[0][0], turn(chessman[0][1]))
        di, dj = DIR[chessman[0][1]]

    if 0 <= i+di < N and 0 <= j+dj < N:
        if MAP[i+di][j+dj] == 0:
            board[i+di][j+dj].extend(chessman)
        elif  MAP[i+di][j+dj] == 1:
            board[i+di][j+dj].extend(chessman[::-1])
        else:
            board[i][j].extend(chessman)
    else:
        board[i][j].extend(chessman)

    if 0 <= i+di < N and 0 <= j+dj < N:
        return len(board[i+di][j+dj])
    else:
        return 0

for i in range(K):
    x, y, d = map(int, input().split())
    board[x-1][y-1].append((i+1, d-1))

while cnt < 1000:
    cnt += 1
    temp = 0

    for x in range(K):
        i, j, k = findIndex(x+1)
        temp = move(i, j, k)
        if temp >= 4:
            break

    if temp >= 4:
        break

print(-1 if cnt == 1000 else cnt)