from collections import deque
r,c = map(int,input().split())
graph = []
#다른 dfs와 다르게 백트래킹이 필요하다
for k in range(r):
  a = input()
  tmp = []
  for u in a:
    tmp.append(u)
  graph.append(tmp)
visited = [[False]*c for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = [[""]*c for _ in range(r)]
board[0][0] = graph[0][0]
visited[0][0] = True
res = []
def bfs(x,y):
  queue =set([(x,y,graph[x][y])])
  while queue:
    x,y, ans= queue.pop()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx<0 or ny<0 or nx>=r or ny>=c:
        continue
      if graph[nx][ny] not in ans:
        queue.add((nx,ny,ans+graph[nx][ny]))
        res.append(ans)
bfs(0,0)
big = 0
for k in res:
  if len(k)>big:
    big = len(k)
print(big+1)