import copy
n = int(input())
l1 = list(map(int,input().split()))
l3 = copy.deepcopy(l1)
l2 = []
l4 = []
for k in range(3):
  if n == 1:
    break
  if k == 0:
    a = max(l1[k],l1[k+1])
    l2.append(a)
    b = min(l3[k],l3[k+1])
    l4.append(b)
  elif k == 2:
    a = max(l1[k],l1[k-1])
    b = min(l3[k],l3[k-1])
    l2.append(a)
    l4.append(b)
  else:
    a = max(l1[k],l1[k-1],l1[k+1])
    b = min(l3[k],l3[k-1],l3[k+1])
    l2.append(a)
    l4.append(b)
for _ in range(1,n):
  l1 = list(map(int,input().split()))
  l3 = copy.deepcopy(l1)
  for u in range(3):
    l1[u] = l1[u]+l2[u]
    l3[u] = l3[u]+l4[u]
  l2 = []
  l4 = []
  for k in range(3):
    if k == 0:
      a = max(l1[k],l1[k+1])
      l2.append(a)
      b = min(l3[k],l3[k+1])
      l4.append(b)
    elif k == 2:
      a = max(l1[k],l1[k-1])
      l2.append(a)
      b = min(l3[k],l3[k-1])
      l4.append(b)
    else:
      a = max(l1[k],l1[k-1],l1[k+1])
      b = min(l3[k],l3[k-1],l3[k+1])
      l2.append(a)
      l4.append(b)
print(max(l1),end=' ')
print(min(l3))