n,m = map(int,input().split())
graph = []

for _ in range(m):
  tmp = input()
  l1 = []
  for k in range(n):
    l1.append(tmp[k])
  graph.append(l1)
wtotal = 0
btotal = 0
wcount = 0
bcount = 0
# DFS로 풀것. 쭉 따라가면 됨
def DFS(x,y):
  global wtotal
  global btotal
  global wcount
  global bcount
  if x<=-1 or x>=m or y<=-1 or y>=n:
    return False
  if graph[x][y] != 'V':
    if graph[x][y] == 'W' and bcount == 0:
      graph[x][y] ='V'
      wcount = wcount +1
      DFS(x+1,y)
      DFS(x-1,y)
      DFS(x,y+1)
      DFS(x,y-1)
    elif graph[x][y] == 'B' and wcount == 0:
      graph[x][y] ='V'
      bcount = bcount +1
      DFS(x+1,y)
      DFS(x-1,y)
      DFS(x,y+1)
      DFS(x,y-1)

for k in range(m):
  for u in range(n):
    DFS(k,u)
    wtotal = wtotal + (wcount*wcount)
    btotal = btotal + (bcount*bcount)
    bcount = 0
    wcount = 0
print(wtotal, btotal)