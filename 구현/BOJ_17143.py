# G[2] 메모리 140304 KB  시간 344 ms

R, C, M = map(int, input().split())
arr = [[(0, 0, 0) for _ in range(C)] for _ in range(R)]
dir = [[-1,0], [1,0], [0,1], [0,-1]]
ans = 0

def turn(d):
    if d % 2 == 0:
        return d+1
    else:
        return d-1

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1] = (s, d-1, z)

for fisherman in range(C):
    for i in range(R):
        if arr[i][fisherman] != (0,0,0):
            ans += arr[i][fisherman][2]
            arr[i][fisherman] = (0,0,0)
            break

    new_arr = [[(0,0,0) for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] != (0, 0, 0):
                s, d, z = arr[i][j]
                arr[i][j] = (0, 0, 0)

                dx, dy = dir[d]
                x, y = i + dx * s, j + dy * s

                if x < 0 or y < 0:
                    d = turn(d)
                    x, y = abs(x), abs(y)
                
                if x >= R:
                    if int((x-1)/(R-1)) % 2 == 1:
                        d = turn(d)
                        x = R - 2 - (x-1)%(R-1)
                    else:
                        x = (x-1)%(R-1) + 1

                if y >= C:
                    if int((y-1)/(C-1)) % 2 == 1:
                        d = turn(d)
                        y = C - 2 - (y-1)%(C-1)
                    else:
                        y = (y-1)%(C-1) + 1

                if z > new_arr[x][y][2]:
                    new_arr[x][y] = (s, d, z)
    
    arr = [item[:] for item in new_arr]

print(ans)