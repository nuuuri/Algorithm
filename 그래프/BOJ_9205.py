# S[1] 메모리 116500 KB  시간 168 ms

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    store = [tuple(map(int, input().split())) for _ in range(n)]
    end = tuple(map(int, input().split()))
    queue = deque([start])
    visited = [0] * n
    isHappy = False

    while queue:
        x, y = queue.popleft()

        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            isHappy = True
            break

        for idx in range(len(store)):
            i, j = store[idx]

            if abs(x-i) + abs(y-j) <= 1000 and not visited[idx]:
                queue.append((i, j))
                visited[idx] = 1

    print('happy' if isHappy else 'sad')