S = int(input())

arr = [0]
arr.extend(map(int, input().split()))
arr.append(float('inf'))

n = int(input())
dic = dict()

num_range = []
for i in range(S+1):
    num_range.append((arr[i], arr[i+1]))
num_range.sort(key = lambda x : x[1] - x[0])

for num in arr[1:-1]:
    dic[num] = 0

print(num_range)


# 이 부분 로직 수정해야 함
for r in num_range[:-1]:
    start, end = r[0]+1, r[1]-1
    for num in range(start, end + 1):
        dic[num] = (num - start) * (end - num + 1) + (end - num)

""" for r in num_range[:-1]:
    for i in range(r[0]+1, r[1]):
        if i not in dic:
            dic[i] = 0

        for j in range(i+1, r[1]):
            for num in range(i, j+1):
                if num in dic:
                    dic[num] += 1
                else:
                    dic[num] = 1
 """
print(dic)
dic = sorted(dic.items(), key = lambda x :( x[1], x[0]))[:n]

for num in dic:
    print(num[0], end = ' ')

for i in range(n - len(dic)):
    print(num_range[-1][0] + i + 1, end = ' ')