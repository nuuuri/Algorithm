# G[2] 메모리 1392932 KB  시간 1112 ms

import sys

DICE = list(map(int, sys.stdin.readline().split()))
graph = [
    [i*2 for i in range(21)], 
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40]]
nodes = [(0, 0), (0, 0), (0, 0), (0, 0)]
ans = 0

def isVisited(arr, x, y):
    if (x, y) in arr:
        return True

    if x == 0 and y % 5 == 0 and y < 20 and (int(y / 5), 0) in arr:
        return True

    if graph[x][y] == 40:
        if (0, 20) in arr or (1, 7) in arr or (2, 6) in arr or (3, 7) in arr:
            return True

    if x in [1, 3] and y >= 4:
        if (1, y) in arr or (2, y-1) in arr or (3, y) in arr:
            return True
    
    if x == 2 and y >= 3:
        if (1, y+1) in arr or (2, y) in arr or (3, y+1) in arr:
            return True

    return False

def solv(arr, idx, cnt):
    global ans

    if idx >= 10:
        if cnt > ans:
            ans = cnt
        return

    for i in range(4):
        x, y = arr[i]
        _arr = arr[:]
        cost = 0

        if y >= len(graph[x]): # 이미 도착한 말
            continue
        
        if y + DICE[idx] < len(graph[x]) and isVisited(arr, x, y+DICE[idx]): # 이미 말이 있는 경우
            continue

        if y + DICE[idx] < len(graph[x]):
            cost = graph[x][y+DICE[idx]]
        
        y += DICE[idx]

        if x == 0 and y%5 == 0 and y < 20: # 갈림길에 도착한 경우
            x, y = int(y/5), 0

        _arr[i] = (x, y)
        solv(_arr, idx+1, cnt + cost)

solv(nodes, 0, 0)
print(ans)