INF = int(1e9)
n, m, r = map(int,input().split())
items = [0]
l1 = list(map(int,input().split()))
for k in l1:
  items.append(k)
graph = [[] for _ in range(n+1)]
for _ in range(r):
  a, b, c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))
#각 지역에 떨어졌을때, 다른 지역에 도착하려면 몇의 거리가 필요한지 계산
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1,n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i 
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  for i in range(n-1):
    now = get_smallest_node()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost<distance[j[0]]:
        distance[j[0]] = cost
res = 0
for k in range(1,n+1):
  visited = [False]*(n+1)
  distance = [INF] * (n+1)
  dijkstra(k)
  total = 0
  for u in range(n+1):
    if distance[u] <= m: 
      total = total + items[u]
  res = max(res,total)
print(res)
  