# G[2] 메모리 31140 KB  시간 164 ms

import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def findMainBlock(block_list):
    for x, y in sorted(block_list):
        if arr[x][y] > 0:
            return (x, y)

def findBlockGroup():
    block_group = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    main = (-1, -1)
    rainbow = -1

    for i in range(N):
        for j in range(N):
            if arr[i][j] <= 0 or visited[i][j]:
                continue

            block_list = []
            queue = [(i, j)]
            visited[i][j] = True
            cnt = 0

            while queue:
                x, y = queue.pop(0)

                if (x, y) in block_list:
                    continue

                if arr[x][y] == 0:
                    cnt += 1

                block_list.append((x, y))

                for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if 0 <= x+dx < N and 0 <= y+dy < N:
                        if arr[x+dx][y+dy] == 0 and (x+dx, y+dy) not in block_list:
                            queue.append((x+dx, y+dy))
                        elif arr[x+dx][y+dy] == arr[i][j] and not visited[x+dx][y+dy]:
                            visited[x+dx][y+dy] = True
                            queue.append((x+dx, y+dy))

            x, y = findMainBlock(block_list)

            if len(block_list) < len(block_group):
                continue
                
            if len(block_list) == len(block_group):
                if cnt < rainbow:
                    continue
                if main > (x, y):
                    continue
            
            block_group = block_list
            main = (x, y)
            rainbow = cnt

    return block_group

def gravity():
    global arr
    temp = list(map(list, zip(*arr)))

    for t in temp:
        for idx in reversed(range(N)):
            if t[idx] < 0:
                continue

            i = idx
            while i < N-1 and t[i+1] == -2:
                i += 1

            if i > idx:
                t[i] = t[idx]
                t[idx] = -2

    arr = copy.deepcopy(list(map(list, zip(*temp))))

def autoPlay():
    global ans, arr

    while True:
        block_group = findBlockGroup()

        if len(block_group) < 2:
            break

        cnt = 0
        for x, y in block_group:
            arr[x][y] = -2
            cnt += 1

        ans += pow(cnt, 2)

        gravity()
        arr = copy.deepcopy(list(map(list, zip(*arr)))[::-1])
        gravity()

autoPlay()
print(ans)