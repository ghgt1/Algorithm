s, p = map(int,input().split())
l1 = list(map(str,input()))
a,c,g,t = map(int,input().split())
total = 0
#고정된 크기만 보므로. 슬라이딩 윈도우로 풀자.
#매번 check가 아닌 개수를 계속 저장하고 있다면?
li1 = l1[0:p]
count = [li1.count('A'),li1.count('C'),li1.count('G'),li1.count('T')]
if count[0]>=a and count[1]>=c and count[2]>=g and count[3]>=t:
  total = total + 1
for k in range(1,s):
  if k+p<=s:
    if l1[k-1] == 'A':
      count[0] = count[0]-1
    elif l1[k-1] == 'C':
      count[1] = count[1] -1
    elif l1[k-1] == 'G':
      count[2] = count[2] - 1
    elif l1[k-1] == 'T':
      count[3] = count[3] - 1
    if l1[k+p-1] == 'A':
      count[0] = count[0]+1
    elif l1[k+p-1] == 'C':
      count[1] = count[1] +1
    elif l1[k+p-1] == 'G':
      count[2] = count[2] + 1
    elif l1[k+p-1] == 'T':
      count[3] = count[3] + 1

    if count[0]>=a and count[1]>=c and count[2]>=g and count[3]>=t:
      total = total + 1
    
print(total)