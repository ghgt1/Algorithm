import math
from collections import deque
n,l,r = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))
#BFS로 탐색
dx = [0,0,1,-1]
dy = [1,-1,0,0]
res = 0
while(True):
  l1 = []
  flag = True
  visited = [[False for _ in range(n)]for u in range(n)]
  for k in range(n):
    for u in range(n):
      if visited[k][u] == False:
        visited[k][u] = True
        queue = deque()
        temp = []
        temp.append((k,u))
        queue.append((k,u))
        while queue:
          x, y = queue.pop()
          for q in range(4):
            nx = x+dx[q]
            ny = y+dy[q]
            if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny] ==True:
              continue
            if r>=abs(graph[x][y]-graph[nx][ny])>=l:
              visited[nx][ny] = True
              queue.append((nx,ny))
              temp.append((nx,ny))
        #사실 모든 국경을 열고 인구이동해야하지만. 국경을 열어야하는 경우이기만 하면 바로 적용해주는 것이 이론적으로 더 효율이 좋다
        total = 0
        count = 0
        if len(temp)>1:
          flag = False
          for q in temp:
            a,b = q
            total = total + graph[a][b]
            count = count + 1
          for q in temp:
            a, b = q
            graph[a][b] = math.trunc(total/count)
  if flag:
    break
  else:
    res = res+1
print(res)