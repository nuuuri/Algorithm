# Algorithm

코딩테스트 알고리즘 문제풀이

## 2차원 리스트 90도 회전

### 1. 시계 방향으로 회전

```python
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist[::-1])))
```

### 2. 반시계 방향으로 회전

```python
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))[::-1]
```

## 달팽이 배열

```python
def snail(n):
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pos = []
    x, y = 0, -1
    d = 0

    while n > 0:
        for _ in range(n):
            x += move[d][0]
            y += move[d][1]
            pos.append((x, y))

        n -= 1
        d = (d+1) % 4

        for _ in range(n):
            x += move[d][0]
            y += move[d][1]
            pos.append((x, y))

        d = (d+1) % 4

    return pos
```
