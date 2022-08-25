# G[5] 메모리 30840 KB  시간 304 ms

import sys
input = sys.stdin.readline

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
students = {}
ans = 0

for _ in range(pow(N,2)):
    temp = list(map(int, input().split()))
    student = temp[0]
    like = temp[1:]
    students[student] = like

    x, y = -1, -1
    adj, empty = -1, -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                continue

            a, e = 0, 0
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if 0 <= i+di < N and 0 <= j+dj < N:
                    if arr[i+di][j+dj] == 0:
                        e += 1
                    if arr[i+di][j+dj] in like:
                        a += 1
            
            if a > adj:
                adj = a
                empty = e
                x, y = i, j
            elif a == adj and e > empty:
                empty = e
                x, y = i, j

    arr[x][y] = student

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            continue

        cnt = 0
        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if 0 <= i+di < N and 0 <= j+dj < N and arr[i+di][j+dj] in students[arr[i][j]]:
                cnt += 1
        
        if cnt > 0:
            ans += pow(10, cnt-1)

print(ans)