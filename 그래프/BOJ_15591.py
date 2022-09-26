# G[5] 메모리 123108 KB  시간 1484 ms

import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().split())
graph = {x:[] for x in range(N)}

for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    graph[p-1].append((q-1, r))
    graph[q-1].append((p-1, r))

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    
    queue = deque([v-1])
    visited = [0]*N
    visited[v-1] = 1
    cnt = 0

    while queue:
        x = queue.popleft()

        if x != v-1:
            cnt += 1
            
        for next, r in graph[x]:
            if r >= k and not visited[next]:
                queue.append(next)
                visited[next] = 1
        
    print(cnt)