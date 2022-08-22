# BFS

### 거리가 같을 때, 우선순위가 ↑ ← → ↓ 순인 경우

queue에서 pop 하기 전에 sort를 해야함

```python
while queue:
    queue.sort(key = lambda x: (x[2], x[0], x[1]))
    x, y, cost = queue.pop(0)
```
