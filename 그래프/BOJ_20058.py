# G[4] 메모리 129188 KB  시간 1028 ms

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(pow(2, N))]
ans, max_ice = 0, 0

def rotate(arr):
    return list(map(list, zip(*arr[::-1])))

def firestorm(level):
    for i in range(0, pow(2, N), pow(2, level)):
        for j in range(0, pow(2, N), pow(2, level)):
            temp = [a[j:j+pow(2, level)] for a in arr[i:i+pow(2, level)]]
            temp = list(map(list, zip(*temp[::-1])))

            for di, t in enumerate(temp):
                for dj, val in enumerate(t):
                    arr[i+di][j+dj] = val

for level in map(int, input().split()):
    firestorm(level)

    temp = [a[:] for a in arr]
    for i in range(pow(2, N)):
        for j in range(pow(2, N)):
            if arr[i][j] == 0:
                continue

            cnt = 0

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i+di < pow(2, N) and 0 <= j+dj < pow(2, N) and temp[i+di][j+dj] > 0:
                    cnt += 1

            if cnt < 3:
                arr[i][j] -= 1

visited = [[False for _ in range(pow(2, N))] for _ in range(pow(2, N))]
for i in range(pow(2, N)):
    for j in range(pow(2, N)):
        if not visited[i][j] and arr[i][j] > 0:
            queue = [(i, j)]
            visited[i][j] = True
            ice_sum = 0
            cnt = 0

            while queue:
                x, y = queue.pop(0)
                ice_sum += arr[x][y]
                cnt += 1

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= x+dx < pow(2,N) and 0 <= y+dy < pow(2,N) and arr[x+dx][y+dy] > 0 and visited[x+dx][y+dy] == False:
                        queue.append((x+dx, y+dy))
                        visited[x+dx][y+dy] = True
                
            ans += ice_sum
            if max_ice < cnt:
                max_ice = cnt

print(ans)
print(max_ice)