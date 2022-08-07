# 최단 경로 알고리즘
import heapq

graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'C': 3, 'D': 2},
    'C': {'B': 3, 'F': 5},
    'D': {'C': 3, 'E': 1},
    'E': {'C': 1, 'F': 2},
    'F': {}
}

def dijkstra(start):
    # 초기 배열 설정 : 자기 자신만 0, 나머지는 inf
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    queue = []

    # 우선순위큐(heapq)가 첫 번째 데이터를 기준으로 정렬하기 때문에 (거리, 노드) 순으로 넣음
    heapq.heappush(queue, (dist[start], start))

    while queue:
        # 가장 짧은 거리와 노드
        current_dist, node = heapq.heappop(queue)

        if current_dist > dist[node]:
            continue

        for next_node, next_dist in graph[node].items():
            cost = current_dist + next_dist
            if dist[next_node] > cost:
                dist[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    return dist
                
print(dijkstra('A'))