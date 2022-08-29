import heapq

# 최소 힙
min_heap = []

heapq.heappush(min_heap, 11)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 30)

print(heapq.heappop(min_heap)) # 5
print(heapq.heappop(min_heap)) # 11
print(heapq.heappop(min_heap)) # 30

# 최대 힙
max_heap = []

heapq.heappush(max_heap, -11)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -30)

print(-heapq.heappop(max_heap)) # 30
print(-heapq.heappop(max_heap)) # 11
print(-heapq.heappop(max_heap)) # 5
