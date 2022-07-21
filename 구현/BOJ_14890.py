# [골드3] 메모리 30840 KB  시간 76 ms

n, l = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = list(map(list, zip(*arr1)))
ans = 0

def checkRoad(list):
    isOK = [True for _ in list]
    
    for i in range(n-1):
        if list[i+1] == list[i]:
            continue
        elif list[i+1] == list[i] + 1 and i - l + 1 >= 0:
            for cnt in range(l):
                if list[i-cnt] == list[i+1] - 1 and isOK[i-cnt] == True:
                    isOK[i-cnt] = False
                else:
                    return 0
        elif list[i+1] == list[i] - 1 and i + l < n:
            for cnt in range(l):
                if list[i+1+cnt] == list[i] - 1 and isOK[i+1+cnt]:
                    isOK[i+1+cnt] = False
                else: return 0
        else:
            return 0
    return 1

for i in range(n):
    ans = ans + checkRoad(arr1[i]) + checkRoad(arr2[i])

print(ans)