# G[4] 메모리 117756 KB  시간 432 ms

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = -1

for x in range(0, N-2):
    for y in range(1, N-1):
        for d1 in range(1, y+1):
            for d2 in range(1, N - y):
                if x + d1 + d2 < N:
                    population = [0, 0, 0, 0, 0]

                    for i in range(N):
                        for j in range(N):
                            if x+y <= i+j <= x+y+d2*2 and x-y <= i-j <= x-y+d1*2:
                                population[4] += arr[i][j]
                            elif 0 <= i < x+d1 and 0 <= j <= y:
                                population[0] += arr[i][j]
                            elif 0 <= i <= x+d2 and y < j < N:
                                population[1] += arr[i][j]
                            elif x+d1 <= i < N and 0 <= j < y-d1+d2:
                                population[2] += arr[i][j]
                            elif x+d2 < i < N and y-d1+d2 <= j < N:
                                population[3] += arr[i][j]

                    temp = max(population) - min(population)
                    
                    if ans == -1 or ans > temp:
                        ans = temp

print(ans)