#모르겠음 망함
import sys
from collections import deque
n = int(input())
color2 = list(map(int,sys.stdin.readline().split()))
color = [[] for _ in range(n+1)]
for k in range(len(color2)):
  color[color2[k]].append(k+1)
graph = [[] for _ in range(n+1)]
child = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
#bfs
queue = deque()
queue.append(1)
visited = [False] * (n+1)
visited[1] = True
#자식관계를 확인
while queue:
  a = queue.popleft()
  for i in graph[a]:
    if not visited[i]:
      child[a].append(i)
      queue.append(i)
      visited[i] = True
total = 0
if color2[0] != 0:
  total = total + 1
for k in range(1,len(child)):
  for u in child[k]:
    if color2[k-1] != color2[u-1]:
      total = total + 1
#print(child)
print(total)