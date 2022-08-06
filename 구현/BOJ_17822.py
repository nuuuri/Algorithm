# G[3] 메모리 30840 KB  시간 252 ms

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def turnDisk(x, d, k):
    for idx in range(N):
        if (idx+1) % x == 0:
            if  d == 0:
                arr[idx] = arr[idx][-k:] + arr[idx][:-k]
            else:
                arr[idx] = arr[idx][k:] + arr[idx][:k]

def removeNumber():
    global arr

    temp = [item[:] for item in arr]
    isValid = False

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'x':
                continue

            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= i+di < N and arr[i+di][(j+dj)%M] == arr[i][j]:
                    temp[i][j] = 'x'
                    temp[i+di][(j+dj)%M] = 'x'
                    isValid = True
    
    arr = [item[:] for item in temp]

    return isValid

def average():
    cnt = 0
    sum = 0
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 'x':
                cnt += 1
                sum += arr[i][j]

    return sum / cnt if cnt > 0 else 0

for _ in range(T):
    x, d, k = map(int, input().split())
    turnDisk(x, d, k)

    if not removeNumber():
        avg = average()

        for i in range(N):
            for j in range(M):
                if arr[i][j] == 'x':
                    continue

                if arr[i][j] > avg:
                    arr[i][j] -= 1
                elif arr[i][j] < avg:
                    arr[i][j] += 1

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 'x':
            ans += arr[i][j]
print(ans)