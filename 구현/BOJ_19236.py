# G[2] 메모리 30840 KB  시간 72 ms

import sys

move = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
space = []
ans = 0

for _ in range(4):
    temp = list(map(int, sys.stdin.readline().split()))
    space.append(list(zip([temp[i*2] for i in range(4)], [temp[i*2+1]-1 for i in range(4)])))

ans += space[0][0][0]
space[0][0] = (-1, space[0][0][1])

def findIdx(arr, fish):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == fish:
                return i, j

    return -1, -1
    
def moveFish(arr):
    for fish in range(1, 17):
        i, j = findIdx(arr, fish)

        if (i, j) == (-1, -1):
            continue

        d = arr[i][j][1]
        isValid = False

        for _ in range(7):
            di, dj = move[d]

            if 0 <= i+di < 4 and 0 <= j+dj < 4 and arr[i+di][j+dj][0] != -1:
                isValid = True
                break
        
            d = (d+1) % 8

        if isValid:
            di, dj = move[d]
            target = arr[i+di][j+dj]

            arr[i+di][j+dj] = (fish, d)
            arr[i][j] = target
    
def solv(arr, cnt):
    global ans

    moveFish(arr)

    i, j = findIdx(arr, -1)
    d = arr[i][j][1]
    
    for t in range(1, 4):
        di, dj = tuple(x*t for x in move[d])

        if 0 <= i+di < 4 and 0 <= j+dj < 4 and arr[i+di][j+dj][0] > 0:
            target = arr[i+di][j+dj]

            if cnt + target[0] > ans:
                ans = cnt + target[0]

            new_arr = [item[:] for item in arr]
            new_arr[i+di][j+dj] = (-1, target[1])
            new_arr[i][j] = (0, 0)

            solv(new_arr, cnt + target[0])

solv(space, ans)
print(ans)