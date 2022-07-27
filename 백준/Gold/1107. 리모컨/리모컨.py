n = int(input())
m = int(input())
l1 = [0,1,2,3,4,5,6,7,8,9]
if m !=0:
  l2 = list(map(int,input().split()))
  for k in l2:
    l1.remove(k)
res = abs(n-100)
for k in range(1000001):
  flag = False
  for u in (str(k)):
    if int(u) not in l1:
      flag = True
      break
  if flag:
    continue
  else:
    res = min(res,abs(k-n) + len(str(k)))
print(res)