import sys
n, p = map(int,input().split())
graph = [[] for _ in range(n+1)]
# stack을 사용하여 각 plat stack의 top이랑 지속적으로 비교.
count = 0
for _ in range(n):
  a,b = map(int,sys.stdin.readline().split())
  if len(graph[a])!=0:
    if b<graph[a][-1]:
      while b<graph[a][-1]:
        graph[a].pop()
        count= count + 1
        if len(graph[a]) == 0:
          break
      if len(graph[a]) == 0:
        graph[a].append(b)
        count = count+1
      else:
        if b!=graph[a][-1]:
          graph[a].append(b)
          count = count + 1
    elif b>graph[a][-1]:
      graph[a].append(b)
      count = count + 1
  else:
    graph[a].append(b)
    count = count + 1
print(count)