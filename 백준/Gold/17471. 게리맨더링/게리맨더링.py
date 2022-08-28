from itertools import combinations
n = int(input())
town = [k for k in range(1,n+1)]
l1 = list(map(int,input().split()))
graph = [[]]
for _ in range(n):
  tmp = list(map(int,input().split()))
  del(tmp[0])
  graph.append(tmp)
def dfs(graph,v,danger,visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      if i in danger:
        continue
      dfs(graph,i,danger,visited)
res = 1000
for k in range(1,n):
  tmp = list(combinations(town,k))
  for u in range(len(tmp)):
    tmp[u] = list(tmp[u])
  tmp2 = []
  for u in tmp:
    tmp3 = []
    for q in town:
      if q not in u:
        tmp3.append(q)
    tmp2.append(tmp3)
  #이어져있는지 판단
  for u in range(len(tmp)):
    flag1 = True
    flag2 = True
    visited = [False] * (n+1)
    visited2 = [False] * (n+1)
    dfs(graph,tmp[u][0],tmp2[u],visited)
    dfs(graph,tmp2[u][0],tmp[u],visited2)
    for q in tmp[u]:
      if visited[q]:
        continue
      else:
        flag1 = False
        break
    for q in tmp2[u]:
      if visited2[q]:
        continue
      else:
        flag2 = False
        break
    total1 = 0
    total2 = 0
    if flag1 and flag2:
      for q in tmp[u]:
        total1 = total1 + l1[q-1]
      for q in tmp2[u]:
        total2 = total2 + l1[q-1]
      res = min(res,abs(total1-total2))
if res!=1000:
  print(res)
else:
  print(-1)