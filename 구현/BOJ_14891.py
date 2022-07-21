# [골드5] 메모리 30840 KB  시간 76 ms

wheel = [list(map(int, list(input()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    w, d = map(int, input().split())
    isTurn = [0 for _ in range(4)]
    isTurn[w - 1] = d

    # 1. 회전 유무 구하기
    for i in reversed(range(w-1)):
        if wheel[i][2] == wheel[i+1][6]:
            continue
        else:
            isTurn[i] = -1 * isTurn[i+1]

    for i in range(w, 4):
        if wheel[i][6] == wheel[i-1][2]:
            continue
        else:
            isTurn[i] = -1 * isTurn[i-1]

    # 2. 각자 회전
    for i in range(4):
        if isTurn[i] == 1:
            wheel[i] = [wheel[i][-1]] + wheel[i][:-1]
        elif isTurn[i] == -1:
            _temp = wheel[i].pop(0)
            wheel[i].append(_temp)

print(sum([wheel[i][0] * 2**i for i in range(4)]))