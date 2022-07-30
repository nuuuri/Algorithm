# G[4] 메모리 120112 KB  시간 640 ms

R, C, T = map(int, input().split())
arr = [[0 for _ in range(C)] for _ in range(R)]
purifier = []

for i in range(R):
    for j, val in enumerate(map(int, input().split())):
        arr[i][j] = val

        if val == -1:
            purifier.append((i,j))

for _ in range(T):
    # 먼지 확산
    temp = [item[:] for item in arr]
    for x in range(R):
        for y in range(C):
            if temp[x][y] > 0:
                dust = int(temp[x][y] / 5)

                for dx, dy in [[-1,0], [0,-1], [0,1], [1,0]]:
                    if 0 <= x+dx < R and 0 <= y+dy < C and temp[x+dx][y+dy] >= 0:
                        arr[x+dx][y+dy] += dust
                        arr[x][y] -= dust
    
    # 위쪽 공기청정기
    x, y = purifier[0][0]-1, purifier[0][1]
    while (x, y) != purifier[0]:
        if x > 0 and y == 0:
            xx, yy = x-1, y
        elif x == 0 and y < C-1:
            xx, yy = x, y+1
        elif x < purifier[0][0] and y == C-1:
            xx, yy = x+1, y
        else:
            xx, yy = x, y-1

        if arr[xx][yy] == -1:
            arr[x][y] = 0
        else:
            arr[x][y] = arr[xx][yy]

        x, y = xx, yy

    # 아래쪽 공기청정기
    x, y = purifier[1][0]+1, purifier[1][1]
    while (x, y) != purifier[1]:
        if x < R-1 and y == 0:
            xx, yy = x+1, y
        elif x == R-1 and y < C-1:
            xx, yy = x, y+1
        elif x > purifier[1][0] and y == C-1:
            xx, yy = x-1, y
        else:
            xx, yy = x, y-1

        if arr[xx][yy] == -1:
            arr[x][y] = 0
        else:
            arr[x][y] = arr[xx][yy]

        x, y = xx, yy

print(sum([sum(item) for item in arr]) + 2)