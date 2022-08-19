# G[2] 메모리 30840 KB  시간 1708 ms

import sys

MOVE = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 위 아 왼 오
N, M, K = map(int, sys.stdin.readline().split())
space = [[[0, 0] for _ in range(N)] for _ in range(N)]
shark = {idx: [-1, -1, -1] for idx in range(1, M+1)}
shark_priority = [[]]

for i in range(N):
    for j, val in enumerate(map(int, sys.stdin.readline().split())):
        if val > 0:
            shark[val] = [i, j, -1]

for i, val in enumerate(map(int, sys.stdin.readline().split())):
    shark[i+1][2] = val-1

for idx in range(M):
    shark_priority.append([list(map(lambda x : int(x)-1, sys.stdin.readline().split())) for _ in range(4)])

def spray():
    for idx in range(1, M+1):
        if idx not in shark:
            continue

        i, j = shark[idx][0], shark[idx][1]
        space[i][j] = [idx, K]

def moveShark(idx):
    if idx not in shark:
        return

    i, j, d = shark[idx]
    priority = shark_priority[idx][d]

    # 빈 공간이 있는 경우
    for p in range(4):
        di, dj = MOVE[priority[p]]

        if 0 <= i+di < N and 0 <= j+dj < N and space[i+di][j+dj] == [0, 0]:
            shark[idx] = [i+di, j+dj, priority[p]]
            return

    # 자신의 냄새가 있는 곳으로
    for p in range(4):
        di, dj = MOVE[priority[p]]

        if 0 <= i+di < N and 0 <= j+dj < N and space[i+di][j+dj][0] == idx:
            shark[idx] = [i+di, j+dj, priority[p]]
            return

def fadeOut():
    for i in range(N):
        for j in range(N):
            if space[i][j][0] > 0:
                space[i][j][1] -= 1

                if space[i][j][1] == 0:
                    space[i][j] = [0, 0]

def solv():
    for idx in range(1, M+1):
        moveShark(idx)

    fadeOut()

    for idx in range(M, 0, -1):
        if idx not in shark:
            continue

        shark_list = list(map(lambda x: x[1][:2], filter(lambda x: x[0] != idx, shark.items())))
        if shark[idx][:2] in shark_list:
            del shark[idx]

    spray()
        
spray()

time = 0
while len(shark) > 1 and time <= 1000:
    solv()
    time += 1

print(-1 if time > 1000 else time)