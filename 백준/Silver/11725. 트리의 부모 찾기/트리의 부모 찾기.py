from collections import deque
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)
parent = [False] * (n+1)
start = 1
dic = {}
queue = deque()
queue.append(1)
while queue:
  start = queue.popleft()
  parent[start] = True
  for k in tree[start]:
    if not parent[k]:
      queue.append(k)
      dic[k] = start
for k in range(2,n+1):
  print(dic[k])