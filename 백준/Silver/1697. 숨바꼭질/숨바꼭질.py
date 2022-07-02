from collections import deque
n,k = map(int,input().split())
count = 0
graph = [0 for u in range(100001)]
graph[n] = 1
# 이건 BFS
l1 = deque()
l1.append(n)
while(True):
  if graph[k] == 1:
    break
  tmp = len(l1)
  for _ in range(tmp):
    a = l1.popleft()
    if a<100000:
      if graph[a+1] == 0:
        graph[a+1] = 1
        l1.append(a+1)
    if 2*a<=100000:
      if graph[2*a] == 0:
        graph[2*a] = 1
        l1.append(2*a)
    if a>0:
      if graph[a-1] == 0:
        graph[a-1] = 1
        l1.append(a-1)
  count = count+1
print(count)