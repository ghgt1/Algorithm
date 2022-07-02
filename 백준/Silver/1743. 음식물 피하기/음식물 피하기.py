from collections import deque
n,m,k = map(int,input().split())
graph=[[0 for _ in range(m)]for u in range(n)]
visited=[[False for _ in range(m)]for u in range(n)]
for u in range(k):
  a, b = map(int,input().split())
  graph[a-1][b-1] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
l1 = [1]
#이어져있는걸 찾으면 됨.
def BFS(x,y):
  queue = deque()
  count = 1
  queue.append((x,y))
  while queue:
    a,b = queue.popleft()
    visited[a][b] = True
    for t in range(4):
      nx = a + dx[t]
      ny = b + dy[t]
      if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny] == True:
        continue
      if graph[nx][ny] == 1:
        queue.append((nx,ny))
        visited[nx][ny] = True
        count = count+1
  l1.append(count)
for q in range(n):
  for u in range(m):
    if graph[q][u] == 1 and visited[q][u] == False:
      BFS(q,u)
print(max(l1))