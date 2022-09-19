# P[5] 메모리 318304 KB  시간 1708 ms
# 일반 BFS 사용하면 시간 초과

import sys
from collections import deque
input = sys.stdin.readline

MOVE = [(1, 0), (0, 1), (-1, 0), (0, -1)]
R, C = map(int, input().split())
arr = []
swan = []
ans = 0
# 백조 이동 확인하는 bfs
swan_queue = deque([])
swan_visited = [[False for _ in range(C)] for _ in range(R)]
# 녹을 얼음 확인하는 bfs
ice_queue = deque([])
ice_visited = [[False for _ in range(C)] for _ in range(R)]

def canMeetSwans():
    global swan_queue
    temp = []

    while swan_queue:
        x, y = swan_queue.popleft()

        if (x, y) == swan[1]:
            return True

        for dx, dy in MOVE:
            if 0 <= x+dx < R and 0 <= y+dy < C and not swan_visited[x+dx][y+dy]:
                swan_visited[x+dx][y+dy] = True
                if arr[x+dx][y+dy] == 'X':
                    temp.append((x+dx, y+dy))
                else:
                    swan_queue.append((x+dx, y+dy))
                
    swan_queue = deque(temp)
    return False

def melt():
    global ice_queue
    temp = []

    while ice_queue:
        x, y = ice_queue.popleft()
        arr[x][y] = '.'

        for dx, dy in MOVE:
            if 0 <= x+dx < R and 0 <= y+dy < C and not ice_visited[x+dx][y+dy]:
                ice_visited[x+dx][y+dy] = True
                if arr[x+dx][y+dy] == 'X':
                    temp.append((x+dx, y+dy))
                else:
                    ice_queue.append((x+dx, y+dy))

    ice_queue = deque(temp)

for r in range(R):
    temp = list(input().strip())
    arr.append(temp)

    for c in range(C):
        if temp[c] == 'L':
            swan.append((r, c))
            arr[r][c] = '.'

for i in range(R):
    for j in range(C):
        if arr[i][j] == '.' and not ice_visited[i][j]:
            ice_queue.append((i, j))
            ice_visited[i][j] = True

swan_queue.append(swan[0])
swan_visited[swan[0][0]][swan[0][1]] = True
melt()

while True:
    if canMeetSwans():
        break

    ans += 1
    melt()

print(ans)