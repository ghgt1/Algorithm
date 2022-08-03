import sys
import bisect
n = int(input())
l1 = list(map(int,sys.stdin.readline().split()))
l1.sort()
res = []
res2 = []
for k in l1:
  pos = bisect.bisect(l1, -(k))
  if pos == n:
    if k!= l1[-1]:
      res.append([k,l1[-1]])
  elif pos == 0:
    if k!=l1[0]:
      res.append([k,l1[0]])
  else:
    if k!=l1[pos]:
      res.append([k,l1[pos]])
    if k!=l1[pos-1]:
      res.append([k,l1[pos-1]])
big = 2000000000
a, b = res[0][0], res[0][1]
for k in res:
  if abs(k[0]+k[1]) < big:
    a = k[0]
    b = k[1]
    big = abs(k[0]+k[1])
if a>b:
  print(b,a)
else:
  print(a,b)