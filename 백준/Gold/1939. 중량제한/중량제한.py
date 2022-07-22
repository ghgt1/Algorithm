# 시간초과 나옴. 보니까 이분탐색으로 기가 막히게 풀 수 있네요
# 도대체 어케 떠올린담?
# 아래는 틀린코드
from collections import deque
INF = int(1e9)
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
max_weight = 0
for _ in range(m):
  a, b, c = map(int,input().split())
  if c > max_weight:
    max_weight = c
  graph[a].append((b,c))
  graph[b].append((a,c))
queue = deque()
begin, finish = map(int,input().split())
visited = [False]*(n+1)
l1 = []
res = 0
def parametric_search(start,end):
  global res
  if start>end:
    return None
  mid = (start+end)//2
  if bfs(graph,begin,visited,mid):
    res = mid
    return parametric_search(mid+1,end)
  else:
    return parametric_search(start, mid-1)
def bfs(graph, v, visited, barrier):
  visited = [False]*(n+1)
  queue = deque()
  queue.append(v)
  visited[v] = True
  while queue:
    v = queue.popleft()
    if v == finish:
      return True
    for a, b in graph[v]:
      if b<barrier:
        continue
      if not visited[a]:
        queue.append(a)
        visited[a] = True
  return False

parametric_search(1, max_weight)
print(res)