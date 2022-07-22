n, m, h = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(h)]
ans = -1

for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[a-1][b] = -1

def result(_arr, idx):
    res = idx
    for i in range(h):
        if _arr[i][res] == 0:
            continue
        else:
            res += _arr[i][res]
    return res

def check(_arr):
    res = []
    for i in range(n):
        res.append(result(_arr, i))
    return res == [x for x in range(n)]

def addLine(_arr, idx, cnt):
    global ans

    if cnt == 4 or idx == h:
        return

    if check(_arr):
        if ans == -1 or ans > cnt:
            ans = cnt
        return 

    addLine(_arr, idx+1, cnt)

    for i in range(n-1):
        new_arr = [item[:] for item in _arr]
        if new_arr[idx][i] == 0 and new_arr[idx][i+1] == 0:
            new_arr[idx][i] = 1
            new_arr[idx][i+1] = -1
            addLine(new_arr, idx+1, cnt+1)

addLine(arr, 0, 0)
print(ans)