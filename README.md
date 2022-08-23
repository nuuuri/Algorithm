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
