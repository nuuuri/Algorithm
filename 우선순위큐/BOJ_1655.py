# G[2] 메모리 36416 KB  시간 276 ms

import sys, heapq
input = sys.stdin.readline

N = int(input())
max_heap, min_heap = [], []

for _ in range(N):
    if len(max_heap) <= len(min_heap):
        heapq.heappush(max_heap, -int(input()))
    else:
        heapq.heappush(min_heap, int(input()))

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        a, b = heapq.heappop(max_heap), heapq.heappop(min_heap)
        heapq.heappush(max_heap, -b)
        heapq.heappush(min_heap, -a)

    print(-max_heap[0])