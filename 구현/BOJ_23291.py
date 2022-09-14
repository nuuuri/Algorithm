# P[5] 메모리 30840 KB  시간 76 ms

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def add_fish(arr):
    min_fish = min(arr)
    for i in range(len(arr)):
        if arr[i] == min_fish:
            arr[i] += 1

def rotate_arr(arr):
    arr = [arr[:1], arr[1:]]
    while len(arr) <= len(arr[-1]) - len(arr[0]):
        temp = arr[-1][len(arr[0]):]
        arr[-1] = arr[-1][:len(arr[0])]

        arr = list(map(list, zip(*arr[::-1])))
        arr.append(temp)

    return arr

def rotate_arr_2(arr):
    temp = [arr]
    for _ in range(2):
        arr_left, arr_right = [], []
        for a in temp:
            arr_left.append(a[:len(a)//2])
            arr_right.append(a[len(a)//2:])

        arr_left = [l[::-1] for l in arr_left[::-1]]
        temp = [*arr_left, *arr_right]

    return temp

def fix_fish(arr):
    diff = [[0 for _ in range(len(a))] for a in arr]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i+di < len(arr) and 0 <= j+dj < len(arr[i+di]):
                    d = abs(arr[i][j] - arr[i+di][j+dj])//5

                    if d > 0:
                        if arr[i][j] > arr[i+di][j+dj]:
                            d *= -1

                        diff[i][j] += d

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] += diff[i][j]

def make_one_line(arr):
    temp = []
    for j in range(len(arr[-1])):
        for i in range(len(arr))[::-1]:
            if 0 <= j < len(arr[i]):
                temp.append(arr[i][j])

    return temp

while True:
    min_fish, max_fish = min(arr), max(arr)
    if max_fish - min_fish <= K:
        break

    ans += 1

    add_fish(arr)
    arr = rotate_arr(arr)
    fix_fish(arr)
    arr = make_one_line(arr)
    arr = rotate_arr_2(arr)
    fix_fish(arr)
    arr = make_one_line(arr)

print(ans)