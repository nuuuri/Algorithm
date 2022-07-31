# G[2] 메모리 116140 KB  시간 128 ms

S = int(input())

arr = [0]
arr.extend(map(int, input().split()))
arr.sort()
arr.append(float('inf'))

n = int(input())
dic = dict()

lucky_set = []
for i in range(S+1):
    lucky_set.append((arr[i], arr[i+1]))
lucky_set.sort(key = lambda x : x[1] - x[0])

for num in arr[1:-1]:
    dic[num] = 0

for lucky in lucky_set[:-1]:
    start = lucky[0] + 1
    end = lucky[1] -1

    for i in range(101):
        for num in set([start + i, end - i]):
            if start <= num <= end and num not in dic:
                dic[num] = (num - start) * (end - num + 1) + (end - num)

dic = sorted(dic.items(), key = lambda x :( x[1], x[0]))[:n]

for num in dic:
    print(num[0], end = ' ')

for i in range(n - len(dic)):
    print(lucky_set[-1][0] + i + 1, end = ' ')