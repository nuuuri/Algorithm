# [G4] 메모리 30840 KB  시간 448 ms

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 99999
cctv=[]
dir = [[0,1], [1,0], [0,-1], [-1,0]]

for i in range(n):
    for j in range(m):
        if 0 < arr[i][j] < 6:
            cctv.append([i,j])

def watch(_arr, i, j, d):
    x, y = i, j
    dx, dy = dir[d % 4]
    while 0 <= x + dx < n and 0 <= y + dy < m:
        x = x + dx
        y = y + dy
        if _arr[x][y] == 6:
            break
        elif _arr[x][y] == 0:
            _arr[x][y] = -1

def dfs(_arr, idx):
    global ans

    if idx == len(cctv):
        cnt = sum([x.count(0) for x in _arr])
        if ans > cnt:
            ans = cnt
        return
    
    i, j = cctv[idx]

    if arr[i][j] == 1:
        for m in range(4):
            new_arr = [item[:] for item in _arr]
            watch(new_arr, i, j, m)
            dfs(new_arr, idx + 1)
    
    elif arr[i][j] == 2:
        for m in range(2):
            new_arr = [item[:] for item in _arr]
            watch(new_arr, i, j, m)
            watch(new_arr, i, j, m+2)
            dfs(new_arr, idx + 1)
    
    elif arr[i][j] == 3:
        for m in range(4):
            new_arr = [item[:] for item in _arr]
            watch(new_arr, i, j, m)
            watch(new_arr, i, j, m+1)
            dfs(new_arr, idx + 1)

    elif arr[i][j] == 4:
        for m in range(4):
            new_arr = [item[:] for item in _arr]
            watch(new_arr, i, j, m)
            watch(new_arr, i, j, m+1)
            watch(new_arr, i, j, m+2)
            dfs(new_arr, idx + 1)
    
    else:
        new_arr = [item[:] for item in _arr]
        for m in range(4):
            watch(new_arr, i, j, m)
        dfs(new_arr, idx + 1)

dfs(arr, 0)
print(ans)