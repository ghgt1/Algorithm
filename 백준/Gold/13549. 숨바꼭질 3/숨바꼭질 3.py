from collections import deque
n,k = map(int,input().split())
count = 0
graph = [0 for u in range(100001)]
graph[n] = 1
count = [0 for u in range(100001)]
# 이건 BFS + DP처럼. count로 dp테이블 사용
l1 = deque()
l1.append(n)
while(True):
  if graph[k] == 1:
    break
  tmp = len(l1)
  for _ in range(tmp):
    a= l1.popleft()
    if 2*a<=100000:
      if graph[2*a] == 0 or count[2*a]>count[a]:
        graph[2*a] = 1
        count[2*a] = count[a]
        l1.appendleft(2*a)
    if a<100000:
      if graph[a+1] == 0:
        graph[a+1] = 1
        count[a+1] = count[a] +1
        l1.append(a+1)
    if a>0:
      if graph[a-1] == 0:
        graph[a-1] = 1
        count[a-1] = count[a] +1
        l1.append(a-1)
print(count[k])