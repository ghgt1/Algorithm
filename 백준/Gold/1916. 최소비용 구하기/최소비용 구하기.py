import heapq
import sys
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
  a, b, c = map(int,sys.stdin.readline().split())
  graph[a].append((b,c))
start, end = map(int,input().split())
#인풋이 크므로 힙을 베이스로한 다익스트라 구현
def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist,now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost<distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
dijkstra(start)
print(distance[end])