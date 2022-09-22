# S[1] 메모리 119696 KB  시간 324 ms

import sys
from collections import deque

N = int(sys.stdin.readline())
arr = []
max_rain = 0
ans = 0

def bfs(rain):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = 1

                while queue:
                    x, y = queue.popleft()

                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if 0 <= x+dx < N and 0 <= y+dy < N and arr[x+dx][y+dy] > rain and not visited[x+dx][y+dy]:
                            queue.append((x+dx, y+dy))
                            visited[x+dx][y+dy] = 1
                
                cnt += 1
    
    return cnt

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
    max_rain = max(max_rain, max(arr[i]))

for rain in range(max_rain + 1):
    result = bfs(rain)

    if result > ans:
        ans = result

print(ans)