from collections import deque
#BFS
#토마토
graph = []
m, n, h = map(int,input().split())
for k in range(h):
  graph.append([])
  for u in range(n):
    graph[k].append(list(map(int,input().split())))

def BFS(graph):
  queue = deque()
  for k in range(h):
    for u in range(n):
      for i in range(m):
        if graph[k][u][i] == 1:
          queue.append((k,u,i))
  while queue:
    x,y,z = queue.popleft()
    move_x = [-1,0,0,0,0,1]
    move_y = [0,0,1,-1,0,0]
    move_z = [0,-1,0,0,1,0]
    for _ in range(6):
      dx = x + move_x[_]
      dy = y + move_y[_]
      dz = z + move_z[_]
      if dx>=0 and dx<h:
        if graph[dx][y][z] == 0:
          graph[dx][y][z] = graph[x][y][z] + 1
          queue.append((dx,y,z))
      if dy>=0 and dy<n:
        if graph[x][dy][z] == 0:
          graph[x][dy][z] = graph[x][y][z] + 1
          queue.append((x,dy,z))
      if dz>=0 and dz<m:
        if graph[x][y][dz] == 0:
          graph[x][y][dz] = graph[x][y][z] + 1
          queue.append((x,y,dz))
BFS(graph)
switch = 0
for k in range(h):
    for u in range(n):
      for i in range(m):
        if graph[k][u][i] == 0 :
          switch = 1
if switch == 0:
  big = graph[0][0][0]
  for k in range(h):
    for u in range(n):
      for i in range(m):
        if graph[k][u][i]>big:
          big = graph[k][u][i]
  print(big-1)
else:
  print(-1)
