# G[4] 메모리 32508 KB  시간 120ms

from collections import Counter

R, C, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(3)]
cnt = 0

def rowSort(arr):
    max_len = 0
    for i in range(len(arr)):
        while 0 in arr[i]:
            arr[i].remove(0)

        temp = []
        for x,y in sorted(Counter(arr[i][:100]).items(), key = lambda x : (x[1], x[0])):
            temp.append(x)
            temp.append(y)
        arr[i] = temp

        if len(temp) > max_len:
            max_len = len(temp)

    for i in range(len(arr)):
        while len(arr[i]) < max_len:
            arr[i].append(0)
    
    return arr
    
def columnSort(arr):
    temp = rowSort(list(map(list, zip(*arr))))

    return list(map(list, zip(*temp)))

while cnt <= 100:
    if R <= len(array) and C <= len(array[0]) and array[R-1][C-1] == K:
        break

    cnt += 1

    if len(array) >= len(array[0]):
        array = rowSort(array)
    else:
        array = columnSort(array)

print(-1 if cnt == 101 else cnt)