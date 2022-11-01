# G[5] 메모리 116684 KB  시간 156 ms
# 0-1 BFS

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

q = deque([(N, 0)])
visited = [0] * 100001
visited[N] = 1

while q:
    num, t = q.popleft()

    if num == K:
        print(t)
        break

    for next in num*2, num+1, num-1:
        if 0 <= next < 100001 and not visited[next]:
            visited[next] = 1

            if next == num*2:
                q.appendleft((next, t))
            else:
                q.append((next, t+1))