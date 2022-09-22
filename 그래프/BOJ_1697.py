# S[1] 메모리 33744 KB  시간 176 ms

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque([(N, 0)])
visited = [False] * 100001

while queue:
    x, cnt = queue.popleft()

    if x == K:
        print(cnt)
        exit(0)

    for next in [x-1, x+1, x*2]:
        if 0 <= next <= 100000 and not visited[next]:
            queue.append((next, cnt+1))
            visited[next] = True