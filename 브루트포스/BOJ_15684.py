# G[3] 메모리 119256 KB  시간 3796 ms

N, M, H = map(int, input().split())
arr = [[0] * N for _ in range(H)]
ans = 4

for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[a-1][b] = -1

def check():
    for n in range(N):
        idx = n

        for h in range(H):
            idx += arr[h][idx]
        
        if idx != n:
            return False
    
    return True


def dfs(x, y, cnt):
    global ans

    if cnt == 4:
        return

    if check() and ans > cnt:
        ans = cnt
        return

    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N-1):
            if arr[i][j] == 0 and arr[i][j+1] == 0:
                arr[i][j] = 1
                arr[i][j+1] = -1

                dfs(i, j+2, cnt+1)

                arr[i][j] = 0
                arr[i][j+1] = 0

dfs(0, 0, 0)
print(ans if ans < 4 else -1)