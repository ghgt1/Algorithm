#탐색 알고리즘 안써도될지도...? 그냥 index로 찾아버리면 될듯!!!!
n,m,s = map(int,input().split())
dic = {}
graph = []
for _ in range(n):
  l1 = list(map(str,input()))
  graph.append(l1)
  for k in l1:
    if k not in dic:
      dic[k] = 1
    else:
      dic[k] = dic[k] + 1
l1 = list(map(str,input()))
dic2 = {}
for k in l1:
  if k not in dic2:
    dic2[k] = 1
  else:
    dic2[k] = dic2[k] + 1
c = 0
res = []
for k in l1:
  if k in dic:
    flag = True
    res.append(dic[k]//dic2[k])
  else:
    flag = False
    break
if flag:
  c = min(res)
if c!=0:
  if min(res) == 0:
    c = 0
def find(f):
  for k in range(n):
    for u in range(m):
      if graph[k][u] == f:
        return (k,u)
cur = (0,0)
res = ""
model = ""
if c!=0:
  for _ in range(c):
    for q in range(s):
      model = model + l1[q]
  for i in range(c*s):
    a, b = find(model[i])
    graph[a][b] = '.'
    if a-cur[0] >0:
      for _ in range(a-cur[0]):
        res = res + 'D'
    elif a-cur[0] <0:
      for _ in range(abs(a-cur[0])):
        res = res + 'U'
    if b-cur[1] >0:
      for _ in range(b-cur[1]):
        res = res + 'R'
    elif b-cur[1] <0:
      for _ in range(abs(b-cur[1])):
        res = res + 'L'
    res = res + 'P'
    cur = (a,b)
a = n-1
b = m-1
if a-cur[0] >0:
  for _ in range(a-cur[0]):
    res = res + 'D'
elif a-cur[0] <0:
  for _ in range(abs(a-cur[0])):
    res = res + 'U'
if b-cur[1] >0:
  for _ in range(b-cur[1]):
    res = res + 'R'
elif b-cur[1] <0:
  for _ in range(abs(b-cur[1])):
    res = res + 'L'
print(c, len(res))
print(res)