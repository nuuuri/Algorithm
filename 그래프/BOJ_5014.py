# G[5] 메모리 128920 KB  시간 268 ms

import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
queue = deque([(S, 0)])
visited = [1 if i == S else 0 for i in range(F+1)]

while queue:
    x, cnt = queue.popleft()

    if x == G:
        print(cnt)
        exit(0)

    for next in [x+U, x-D]:
        if 0 < next <= F and not visited[next]:
            queue.append((next, cnt+1))
            visited[next] = 1

print('use the stairs')
