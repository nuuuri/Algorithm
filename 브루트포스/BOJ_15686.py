# G[5] 메모리 118356 KB  시간 236 ms

N, M  = map(int, input().split())
home_list = []
chicken_list = []
selected = []
ans = 99999

for i in range(N):
    for j, val in enumerate(map(int, input().split())):
        if val == 1:
            home_list.append((i, j))
        elif val == 2:
            chicken_list.append((i, j))

def calculateChickenDist():
    cnt = 0

    for i,j in home_list:
        cnt += min(map(lambda x: abs(i-x[0])+abs(j-x[1]), selected))

    return cnt

def dfs(idx, cnt):
    global ans

    if cnt == M:
        temp = calculateChickenDist()
        if temp < ans:
            ans = temp
        return

    if idx >= len(chicken_list):
        return

    i,j = chicken_list[idx]
    
    selected.append((i,j))
    dfs(idx+1, cnt+1)

    selected.pop()
    dfs(idx+1, cnt)

dfs(0, 0)
print(ans)