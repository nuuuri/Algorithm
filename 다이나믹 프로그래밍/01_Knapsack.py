N = 4 # 물품의 수
K = 7 # 배낭에 담을 수 있는 무게
item = [(2, 3), (4, 3), (5, 2), (3,3)] # (w, c) = (무게, 가치)

def kanpsack():
    # cost[i][j] : 전체 무게가 j를 넘기 않도록 i번째 항목까지 얻어진 최대 이익
    cost = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        w, c = item[i-1]

        for j in range(1, K+1):
            if w <= j:
                cost[i][j] = max(cost[i-1][w], cost[i-1][j-w] + c)
            else:
                cost[i][j] = cost[i-1][j]

    for c in cost:
        print(c)
    return cost[N][K]

print(kanpsack())