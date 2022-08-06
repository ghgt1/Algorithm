from collections import deque
graph = []
for _ in range(12):
  graph.append(list(map(str,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  if graph[x][y] == '.':
    return False
  queue = deque()
  bomb = [(x,y)]
  queue.append((x,y))
  t = graph[x][y]
  graph[x][y] = 'Z'
  count = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx<0 or ny<0 or nx>=12 or ny>=6:
        continue
      if graph[nx][ny] == t:
        if (nx,ny) not in queue:
          queue.append((nx,ny))
          graph[nx][ny] = 'Z'
        if (nx,ny) not in bomb:
          bomb.append((nx,ny))
          count = count + 1
      else:
        continue
  if count >=4:
    for k in bomb:
      a, b = k
      graph[a][b] = '.'
    return True
  for k in bomb:
    a,b = k
    graph[a][b] = t
  return False
def down(graph):
  for u in range(6):
    tmp = []
    for k in range(12):
      tmp.append(graph[k][u])
    flag = True
    while flag:
      for k in range(1,12):
        if tmp[k] == '.':
          if tmp[k-1] !='.':
            del tmp[k]
            tmp.insert(0,'.')
            continue
      flag = False
    for k in range(12):
      graph[k][u] = tmp[k]
total = 0
while(True):
  flag2 = False
  l2 = []
  for k in range(12):
    for u in range(6):
      if graph[k][u] !='.':
        l2.append((k,u))
  while l2:
    c,d = l2.pop()
    if bfs(c,d):
      if not flag2:
        flag2 = True
        total = total + 1
  if flag2:
    down(graph)
    #print(graph)
    continue
  else:
    break
print(total)