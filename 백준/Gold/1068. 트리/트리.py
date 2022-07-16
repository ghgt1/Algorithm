from collections import deque
n = int(input())
tree = {}
l1 = list(map(int,input().split()))
for i in range(n):
  tree[i] = l1[i]
a = int(input())
queue = deque()
queue.append(a)
deleted_elements = []
leaf = [[] for _ in range(n)]
for u in range(n):
  if l1[u] != -1:
    leaf[l1[u]].append(u)
while queue:
  a = queue.popleft()
  deleted_elements.append(a)
  for k in range(n):
    if tree[k] == a:
      queue.append(k)
res = []
for k in leaf:
  tmp = 0
  for u in k:
    if u in deleted_elements:
      continue
    else:
      tmp = tmp + 1
  res.append(tmp)
count = 0
for k in range(n):
  if k not in deleted_elements and res[k] == 0:
    count = count + 1
print(count)