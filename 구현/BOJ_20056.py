# G[4] 메모리 218348 KB  시간 1544 ms

import sys, copy

input = sys.stdin.readline

MOVE = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append((m, s, d))

for _ in range(K):
    # 파이어볼 이동
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for m, s, d in arr[i][j]:
                di, dj = MOVE[d][0]*s, MOVE[d][1]*s
                new_arr[(i+di)%N][(j+dj)%N].append((m, s, d))

    # 파이어볼 합치고 나누기
    for i in range(N):
        for j in range(N):
            if len(new_arr[i][j]) < 2:
                continue

            sum_m, sum_s = 0, 0
            is_all_odd = True
            is_all_even = True

            for m, s, d in new_arr[i][j]:
                sum_m += m
                sum_s += s
                if d%2 == 0:
                    is_all_odd = False
                else:
                    is_all_even = False

            m = int(sum_m/5)
            s = int(sum_s/len(new_arr[i][j]))
            new_arr[i][j] = []

            if m == 0:
                continue

            if is_all_odd or is_all_even:
                for d in [0, 2, 4, 6]:
                    new_arr[i][j].append((m, s, d))
            else:
                for d in [1, 3, 5, 7]:
                    new_arr[i][j].append((m, s, d))

    arr = copy.deepcopy(new_arr)

cnt = 0
for i in range(N):
    for j in range(N):
        for f in arr[i][j]:
            cnt += f[0]
print(cnt)