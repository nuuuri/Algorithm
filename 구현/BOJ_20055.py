# G[5] PyPy3 메모리 116184 KB  시간 488 ms / Python3 메모리 30840 KB  시간 2300 ms

import sys

N, K = map(int, sys.stdin.readline().split())
conveyor = list(map(lambda x: [int(x), 0], sys.stdin.readline().split()))
ans = 0
cnt = 0

def leaveConveyor():
    if conveyor[N-1][1] == 1:
        conveyor[N-1][1] = 0

def rotate():
    global conveyor
    conveyor = [conveyor[-1]]+ conveyor[:-1]
    leaveConveyor()

def moveRobot():
    global cnt

    for i in reversed(range(0, N)):
        if conveyor[i][1] == 1 and conveyor[i+1][0] > 0 and conveyor[i+1][1] == 0:
            conveyor[i][1] = 0
            conveyor[i+1] = [conveyor[i+1][0]-1, 1]

            if conveyor[i+1][0] == 0:
                cnt += 1

    leaveConveyor()

while cnt < K:
    ans += 1
    rotate()
    moveRobot()

    if conveyor[0][0] > 0 and conveyor[0][1] == 0:
        conveyor[0] = [conveyor[0][0]-1, 1]

        if conveyor[0][0] == 0:
            cnt += 1

print(ans)