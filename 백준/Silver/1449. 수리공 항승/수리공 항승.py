n, l = map(int,input().split())
l1 = list(map(int,input().split()))
l1.sort()
start = l1[0]
count = 1
end = start + l
for k in range(n):
  if start<=l1[k] and l1[k]<end:
    continue
  else:
    start = l1[k]
    end = l1[k] + l
    count = count + 1
print(count)