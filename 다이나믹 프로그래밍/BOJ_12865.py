# G[5] 메모리 193672 KB  시간 324 ms

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
item = [tuple(map(int, input().split())) for _ in range(N)]

def kanpsack():
    # cost[i][j] : 전체 무게가 j를 넘기 않도록 i번째 항목까지 얻어진 최대 이익
    cost = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        w, c = item[i-1]

        for j in range(1, K+1):
            if w <= j:
                cost[i][j] = max(cost[i-1][j], cost[i-1][j-w] + c)
            else:
                cost[i][j] = cost[i-1][j]

    return cost[N][K]

print(kanpsack())