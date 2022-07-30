# G[3] 메모리 117484 KB  시간 148 ms

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
start = (0,0)
shark = 2
cnt = 0
time = 0

for i in range(N):
    for j, val in enumerate(map(int, input().split())):
        arr[i][j] = val
        if val == 9:
            start = (i,j)

def bfs(i, j, k):
    global time, cnt, shark

    arr[i][j] = 0
    queue = [(i,j,k)]
    visited = [[True if ii == i and jj == j else False for jj in range(N)] for ii in range(N)]

    while queue:
        queue.sort(key = lambda x : (x[2], x[0], x[1]))
        x, y, t = queue.pop(0)

        if 0 < arr[x][y] < shark:
            time = t
            cnt += 1

            if cnt == shark:
                cnt = 0
                shark += 1

            bfs(x, y, t)
            return

        for dx, dy in [[-1,0], [0,-1], [0,1], [1,0]]:
            if 0 <= x+dx < N and 0 <= y+dy < N and visited[x+dx][y+dy] == False and arr[x+dx][y+dy] <= shark:
                queue.append((x+dx, y+dy, t+1))
                visited[x+dx][y+dy] = True

bfs(start[0], start[1], 0)
print(time)