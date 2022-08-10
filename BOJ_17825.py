import sys

DICE = list(map(int, sys.stdin.readline().split()))
graph = [
    [i*2 for i in range(21)], 
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40]]
isVisited = [[False for _ in range(21)] for _ in range(4)]
nodes = [(0, 0), (0, 0), (0, 0), (0, 0)]
ans = 0

def setVisited(visited, x, y, val):
    if y >= len(graph[x]):
        return

    if graph[x][y] == 40:
        visited[0][20] = val
        visited[1][7] = val
        visited[2][6] = val
        visited[3][7] = val
    elif x > 0 and y == 0:
        visited[x][y] = val
        visited[0][5*x] = val
    elif x == 0 and y%5 == 0 and y < 20:
        visited[x][y] = val
        visited[int(y/5)][0] = val
    elif x in [1, 3] and y >= 4:
        visited[1][y] = val
        visited[2][y-1] = val
        visited[3][y] = val
    elif x == 2 and y >= 3:
        visited[1][y+1] = val
        visited[2][y] = val
        visited[3][y+1] = val

def solv(arr, visited, idx, cnt):
    global ans

    if idx >= 10:
        if cnt > ans:
            ans = cnt
        return

    for i in range(4):
        x, y = arr[i]
        _arr, _visited = arr[:], [item[:] for item in visited]
        cost = 0

        if y >= len(graph[x]): # 이미 도착한 말
            continue
        
        if y + DICE[idx] < len(graph[x]) and _visited[x][y+DICE[idx]] == True: # 이미 말이 있는 경우
            continue

        setVisited(_visited, x, y, False)

        if y + DICE[idx] < len(graph[x]):
            cost = graph[x][y+DICE[idx]]
        
        y += DICE[idx]

        if x == 0 and y%5 == 0 and y < 20: # 갈림길에 도착한 경우
            x, y = int(y/5), 0

        setVisited(_visited, x, y, True)
        _arr[i] = (x, y)
    
        solv(_arr, _visited, idx+1, cnt + cost)

solv(nodes, isVisited, 0, 0)
print(ans)