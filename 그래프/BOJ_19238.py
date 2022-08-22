# G[3] 메모리 30840 KB  시간 256 ms

import sys

N, M, fuel = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
taxi = tuple(map(lambda x: int(x)-1, sys.stdin.readline().split()))
passenger = [list(map(lambda x: int(x)-1, sys.stdin.readline().split())) for _ in range(M)]

def findMinDist(i, j):
    queue = [(taxi[0], taxi[1], 0)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[taxi[0]][taxi[1]] = True

    while queue:
        x, y, cost = queue.pop(0)

        if (x, y) == (i, j):
            return cost

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if 0 <= x+dx < N and 0 <= y+dy < N and arr[x+dx][y+dy] == 0 and visited[x+dx][y+dy] == False:
                queue.append((x+dx, y+dy, cost+1))
                visited[x+dx][y+dy] = True

    return float('inf')

def findPassenger():
    queue = [(taxi[0], taxi[1], 0)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[taxi[0]][taxi[1]] = True
    temp = [p[:2] for p in passenger]

    while queue:
        queue.sort(key = lambda x: (x[2], x[0], x[1]))
        x, y, cost = queue.pop(0)

        if [x, y] in temp:
            return temp.index([x, y]), cost

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if 0 <= x+dx < N and 0 <= y+dy < N and arr[x+dx][y+dy] == 0 and visited[x+dx][y+dy] == False:
                queue.append((x+dx, y+dy, cost+1))
                visited[x+dx][y+dy] = True

    return -1, float('inf')

for _ in range(M):
    p, cost = findPassenger()
    
    if p == -1: # 태울 수 있는 승객이 없는 경우
        fuel = -1
        break

    fuel -= cost
    taxi = (passenger[p][0], passenger[p][1])

    if fuel <= 0:
        fuel = -1
        break

    x, y = passenger[p][2], passenger[p][3]
    cost = findMinDist(x, y)

    fuel -= cost

    if fuel < 0:
        fuel = -1
        break

    fuel += cost * 2
    taxi = (x, y)
    passenger.pop(p)

print(fuel)