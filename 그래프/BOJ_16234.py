# G[5] 메모리 132196 KB  시간 1468 ms

N, L, R = map(int, input().split())
arr = [[x for x in map(int, input().split())] for _ in range(N)]
union_list = []
ans = 0

def BFS(i, j):
    queue = []
    temp = []
    queue.append((i, j))
    temp.append((i, j))
    visited[i][j] = True

    while queue:
        x,y = queue.pop(0)
        for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
            if 0 <= x+dx < N and 0 <= y+dy < N and visited[x+dx][y+dy] == False and L <= abs(arr[x][y]-arr[x+dx][y+dy]) <= R:
                    queue.append((x+dx, y+dy))
                    temp.append((x+dx, y+dy))
                    visited[x+dx][y+dy] = True
    
    if len(temp) > 1:
        union_list.append(temp)

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                BFS(i,j)

    if not union_list:
        break

    for union in union_list:
        population = int(sum([arr[x][y] for x,y in union])/len(union))
        for x,y in union:
            arr[x][y] = population

    ans += 1
    union_list.clear()

print(ans)