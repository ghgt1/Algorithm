import sys
n, s = map(int,input().split())
l1 = list(map(int,sys.stdin.readline().split()))
# 투포인터 사용
a, b = 0 , 0
res = []
total = l1[a]
while(a!=n):
  if a >=b:
    if total >=s:
      res.append(b-a+1)
    b = b+1
    if b!= n:
      total = total + l1[b]
  if total >=s or b == n:
    if total>=s:
      res.append(b-a+1)
    a = a+1
    total = total - l1[a-1]
  else:
    b = b+1
    if b!= n:
      total = total + l1[b]
if len(res) == 0:
  print(0)
else:
  print(min(res))