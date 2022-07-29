# G[3] 메모리 152660 KB  시간 888 ms

from collections import deque

N, M, K = map(int, input().split())
A = [[x for x in map(int, input().split())] for _ in range(N)]
arr = [[5 for _ in range(N)] for _ in range(N)]
trees = [[deque([]) for _ in range(N)] for _ in range(N)]
ans = 0

for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

trees = [[deque(sorted(trees[i][j])) for j in range(N)] for i in range(N)]

for _ in range(K):
    # 봄 & 여름
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) == 0:
                continue

            new_trees = deque([])

            while trees[i][j]:
                age = trees[i][j][0]
                if age <= arr[i][j]:
                    arr[i][j] -= age
                    new_trees.append(age + 1)
                    trees[i][j].popleft()
                else:
                    break

            while trees[i][j]:
                age = trees[i][j].popleft()
                arr[i][j] += int(age / 2)

            trees[i][j] = new_trees

    # 가을
    for x in range(N):
        for y in range(N):
            for age in trees[x][y]:
                if age % 5 == 0:
                    for dx, dy in [[-1,-1],[-1,0],[-1,+1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                        if 0 <= x+dx < N and 0 <= y+dy < N:
                            trees[x+dx][y+dy].appendleft(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            arr[i][j] += A[i][j]

for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])

print(ans)