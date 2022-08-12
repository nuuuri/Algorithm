# G[2] 메모리 30840 KB  시간 408 ms

import sys

red = [[0 for _ in range(4)] for _ in range(4)]
blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]
ans = 0

def placeBlock(type, x, y):
    global blue, green, ans

    # blue
    i = 0
    while i < 5:
        if blue[x][i+1] == 1 or (type == 3 and blue[x+1][i+1] == 1):
            break

        i += 1

    if type == 1:
        blue[x][i] = 1
    elif type == 2:
        blue[x][i-1] = 1
        blue[x][i] = 1
    else:
        blue[x][i] = 1
        blue[x+1][i] = 1

    for ii, arr in enumerate(map(list, zip(*blue))):
        temp = list(map(list, zip(*blue)))
        if arr == [1,1,1,1]:
            temp.pop(ii)
            temp.insert(0, [0,0,0,0])
            ans += 1
        blue = list(map(list, zip(*temp)))

    while 1 in [blue[ii][jj] for ii in range(4) for jj in range(2)]:
        blue = [[0] + b[:5] for b in blue]

    # green
    i = 0
    while i < 5:
        if green[i+1][y] == 1 or (type == 2 and green[i+1][y+1] == 1):
            break

        i += 1
    
    if type == 1:
        green[i][y] = 1
    elif type == 2:
        green[i][y] = 1
        green[i][y+1] = 1
    else:
        green[i-1][y] = 1
        green[i][y] = 1

    for ii, arr in enumerate(green):
        temp = [item[:] for item in green]
        if arr == [1,1,1,1]:
            temp.pop(ii)
            temp.insert(0, [0,0,0,0])
            ans += 1
        green = temp

    while 1 in [green[ii][jj] for ii in range(2) for jj in range(4)]:
        green = [[0,0,0,0]] + green[:5]

for _ in range(int(sys.stdin.readline())):
    t, x, y = map(int, sys.stdin.readline().split())
    placeBlock(t, x, y)

cnt = 0
for b in blue:
    cnt += sum(b)
for g in green:
    cnt += sum(g)

print(ans)
print(cnt)