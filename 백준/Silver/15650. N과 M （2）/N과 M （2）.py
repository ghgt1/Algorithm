n, m = map(int,input().split())
answer = []
visited = [False] * (n+1)

def DFS():
  if len(answer) == m:
    print(' '.join(answer))
  for i in range(1,n+1):
    if not visited[i]:
      if len(answer) >0 and i < int(answer[-1]):
        continue
      visited[i] = True
      answer.append(str(i))
      DFS()
      answer.pop()
      visited[i] = False
DFS()