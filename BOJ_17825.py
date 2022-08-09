import sys

graph = [
    [i*2 for i in range(21)], 
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40]]
visited = [[False] * 20, [False] * 8, [False] * 7, [False] * 8]
node = [(0, 0)] * 4
ans = 0

def setVisited(x, y, isVisited):
    if y >= len(graph[x]):
        return

    if x > 0 and y == 0:
        visited[x][y] = isVisited
        visited[0][5*x] = isVisited
    if x == 0 and y%5 == 0 and y < 20:
        visited[x][y] = isVisited
        visited[int(y/5)][0] = isVisited
    if (x, y) in [(1, 4), (2, 3), (3, 4)]:
        for i, j in [(1, 4), (2, 3), (3, 4)]:
            visited[i][j] = isVisited
""" 
def move(num):
    global ans

    cnt = -1
    idx, pos = -1, (0, 0)

    for i in range(4):
        x, y = node[i]
        res = 0

        if graph[x][y] == 40:
            y += 1
        elif y + num >= len(graph[x]):
            res = 40
        else:
            res = graph[x][y+num]

        if res > cnt:
            cnt = res
            idx = i
            pos = x, y+num

    ans += cnt
    setVisited(node[idx][0], node[idx][1], False)
    if pos[0] == 0 and pos[1]%5 == 0 and pos[1] < 20:
        pos = (int(pos[1]/5), 0)
    node[idx] = pos
    setVisited(node[idx][0], node[idx][1], True)

    print(node, ans)
        
for num in map(int, sys.stdin.readline().split()):
    move(num)

print(ans) """