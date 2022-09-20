# G[4] 메모리 115584 KB  시간 128 ms

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
ans = [list(map(int, input().split())) for _ in range(N)]

def multi(arr1, arr2):
    return [[sum(i*j%1000 for i, j in zip(row, col)) for col in zip(*arr2)] for row in arr1]

def pow(arr, n):
    result = [[1 if i==j else 0 for j in range(N)] for i in range(N)]

    while n:
        if n%2:
            result = multi(result, arr)

        arr = multi(arr, arr)
        n //= 2

    return result

ans = pow(ans, B)

for i in ans:
    for j in i:
        print(j % 1000, end = ' ')
    print()