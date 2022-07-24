# G[4] 메모리 115432 KB  시간 164 ms

MOVE = [[0, 1], [-1, 0], [0, -1], [1, 0]]
N = int(input())
arr = [[0] * 101 for _ in range(101)]
ans = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())
    pos = [(y, x), (y+MOVE[d][0], x+MOVE[d][1])]

    for _ in range(g):
        temp = pos[:]
        end = temp.pop()
        while temp:
            current = temp.pop()
            dy, dx = map(lambda x: x[0]-x[1], zip(current, end))
            pos.append((end[0] + dx, end[1] - dy))

    for i,j in pos:
        arr[i][j] = 1

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j] == 1 and arr[i+1][j+1] == 1:
            ans += 1

print(ans)