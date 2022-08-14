import sys
import math
n,m = map(int,input().split())
l1 = []
for _ in range(m):
  l1.append(int(sys.stdin.readline()))
res = max(l1)
def parametric_search(arr,start,end):
  global res
  if start>end:
    return None
  mid = (start+end)//2
  total = 0
  for k in arr:
    total = total + math.ceil(k/mid)
  if total<=n: #더 좁게 탐색
    res = mid
    return parametric_search(arr,start,mid-1)
  else:
    return parametric_search(arr,mid+1,end)
parametric_search(l1,1,max(l1))
print(res)