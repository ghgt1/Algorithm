n,m = map(int,input().split())
l1 = list(map(int,input().split()))
l1.pop(0)
graph = []
for _ in range(m):
  l2 = list(map(int,input().split()))
  l2.pop(0)
  graph.append(l2)
  for k in l2:
    if k in l1:
      l1 = l1+l2
      l1 = list(set(l1))
flag = True
while(flag):
  a = len(l1)
  for u in graph:
    for k in u:
      if k in l1:
        l1 = l1 + u
        l1 = list(set(l1))
  b = len(l1)
  if a==b:
    flag = False
count = 0

def check(a,b):
  for k in b:
    if k in a:
      return True
  return False
for k in graph:
  if check(l1,k):
    continue
  else:
    count = count+1
print(count)
    