n = int(input())
al = []
for _ in range(26):
  al.append(0)
for _ in range(n):
  a = input()
  for k in range(len(a)):
    al[ord(a[k])-ord('A')] = al[ord(a[k])-ord('A')] + 10**(len(a)-k-1)
l1 = [0,1,2,3,4,5,6,7,8,9]
total = 0
al.sort()
al.reverse()
for k in al:
  if k != 0:
    b = l1.pop()
    total = total + (b*k)
print(total)