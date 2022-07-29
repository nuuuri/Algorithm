# G[3] 메모리 152660 KB  시간 1152 ms

N, M, K = map(int, input().split())
A = [[x for x in map(int, input().split())] for _ in range(N)]
arr = [[5 for _ in range(N)] for _ in range(N)]
trees = [[[] for _ in range(N)]for _ in range(N)]
ans = 0

for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

trees = [[sorted(trees[i][j]) for j in range(N)] for i in range(N)]

for _ in range(K):
    # 봄 & 여름
    for i in range(N):
        for j in range(N):
            temp = trees[i][j][:]
            new_trees = []

            while temp:
                age = temp[0]
                if age <= arr[i][j]:
                    arr[i][j] -= age
                    new_trees.append(age + 1)
                    temp.pop(0)
                else:
                    break
            
            while temp:
                age = temp.pop(0)
                arr[i][j] += int(age / 2)

            trees[i][j] = new_trees

    # 가을
    temp = [item[:] for item in trees]
    for x in range(N):
        for y in range(N):
            for tree in temp[x][y]:
                if tree % 5 == 0:
                    for dx, dy in [[-1,-1],[-1,0],[-1,+1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                        if 0 <= x+dx < N and 0 <= y+dy < N:
                            trees[x+dx][y+dy].insert(0, 1)

    # 겨울
    for i in range(N):
        for j in range(N):
            arr[i][j] += A[i][j]

for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])

print(ans)