# S[2] 메모리 113112 KB  시간 104 ms

import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = {x: [] for x in range(1, N+1)}

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(i, j):
    queue = [(i, 0)]
    visited = [True if idx == i else False for idx in range(N+1)]

    while queue:
        x, cnt = queue.pop(0)

        if x == j:
            return cnt

        for next in graph[x]:
            if not visited[next]:
                queue.append((next, cnt+1))
                visited[next] = True

    return -1

print(bfs(A, B))
