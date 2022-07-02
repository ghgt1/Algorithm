from collections import deque
n,m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input())))
#최단경로이므로 BFS 문제로 해결
queue = deque()
queue.append((0,0))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for k in graph:
  for u in range(m):
    if k[u] == 1:
      k[u] = 'A'
graph[0][0] = 0
def BFS(graph):
  while(True):
    x, y =queue.popleft()
    if x==n-1 and y == m-1:
      return graph[n-1][m-1]
    for k in range(4):
      nx = x+dx[k]
      ny = y+dy[k]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] =='A':
        queue.append((nx,ny))
        graph[nx][ny] = graph[x][y] + 1
        continue
print(BFS(graph)+1)