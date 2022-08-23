# G[3] 메모리 119940 KB  시간 948 ms

import sys
input = sys.stdin.readline

MOVE = [(0, -1), (1, 0), (0, 1), (-1, 0)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
i, j = int(N/2), int(N/2)
ans = 0

def moveSand(x, y, d):
    global ans
    sand = arr[x][y]
    arr[x][y] = 0
    total_sand = sand
    temp = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 1, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]

    for percent in [0.01, 0.01, 0.02, 0.02, 0.07, 0.07, 0.1, 0.1, 0.05]:
        total_sand -= int(sand*percent)

    def rotate(arr):
        return list(map(list, zip(*arr[::-1])))

    if d == 1:
        temp = rotate(rotate(rotate(temp)))
    elif d == 2:
        temp = rotate(rotate(temp))
    elif d == 3:
        temp = rotate(temp)

    for i in range(5):
        for j in range(5):
            if temp[i][j] == 0:
                continue

            s = total_sand if temp[i][j] == 1 else int(sand*temp[i][j])
            dx, dy = i-2, j-2

            if 0 <= x+dx < N and 0 <= y+dy < N:
                arr[x+dx][y+dy] += s
            else:
                ans += s

d, s, cnt = 0, 1, 0
while (i, j) != (0, -1):
    i += MOVE[d%4][0]
    j += MOVE[d%4][1]

    moveSand(i, j, d%4)

    cnt += 1
    if cnt == s:
        cnt = 0
        d += 1
        if d%2 == 0:
            s += 1

print(ans)