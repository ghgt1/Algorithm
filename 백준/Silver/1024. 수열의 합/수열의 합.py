a,b = input().split()
a = int(a)
b = int(b)
l1 = []
#홀짝을 나눠야함 b가 홀수면 a/b가 나눠떨어져야함. 아니면 b를1늘린다
#b가 짝수면 .5꼴로 나와야함. 아니면 b를 1늘린다
while(True):
  if b>100:
    break
  if b%2==0:
    if ((a%b)/b==0.5):
      count = (a//b)-(b/2)+1
      for k in range(b):
        l1.append(count)
        count = count + 1
      break
    else:
      b = b+1
  else:
    if(a%b==0):
      count = (a//b)-(b//2)
      for k in range(b):
        l1.append(count)
        count = count + 1
      break
    else:
      b = b+1
for k in range(len(l1)):
  l1[k] = int(l1[k])
if len(l1)>0 and l1[0]>=0:
  print(*l1)
else:
  print(-1)

