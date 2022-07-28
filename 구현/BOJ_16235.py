# G[3]

N, M, K = map(int, input().split())
A = [[x for x in map(int, input().split())] for _ in range(N)]
arr = [[5 for _ in range(N)] for _ in range(N)]
trees = [[[] for _ in range(N)]for _ in range(N)]
ans = 0

for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

for _ in range(K):
    # 1. 봄 & 여름
    for i in range(N):
        for j in range(N):
            trees[i][j].sort()
            cnt = 0
            temp = trees[i][j][:]
            
            for k, age in enumerate(trees[i][j][:]):
                if age <= arr[i][j]:
                    arr[i][j] -= age
                    trees[i][j][k - cnt] += 1
                else:
                    arr[i][j] += int(age / 2)
                    trees[i][j].pop(k - cnt)
                    cnt += 1

    # 3. 가을
    for x in range(N):
        for y in range(N):
            for tree in trees[x][y]:
                if tree % 5 == 0:
                    for dx, dy in [[-1,-1],[-1,0],[-1,+1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                        if 0 <= x+dx < N and 0 <= y+dy < N:
                            trees[x+dx][y+dy].insert(0, 1)

    # 4. 겨울
    for i in range(N):
        for j in range(N):
            arr[i][j] += A[i][j]

for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])

print(ans)