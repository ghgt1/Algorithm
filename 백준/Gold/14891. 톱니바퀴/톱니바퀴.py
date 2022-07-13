import copy
l1 = list(map(int,input()))
l2 = list(map(int,input()))
l3 = list(map(int,input()))
l4 = list(map(int,input()))
n = int(input())
def rotate_1_2(l1,l2,who,dir):
  if who == 1:
    #시계 반시계
    if dir == 1:
      l1.insert(0,l1[-1])
      l1.pop()
      l2.insert(8,l2[0])
      l2.pop(0)
      #2번 톱니의 회전방향
      return -1
    #반시계 시계
    else:
      l1.insert(8,l1[0])
      l1.pop(0)
      l2.insert(0,l2[-1])
      l2.pop()
      return 1
  #반시계 시계  
  else:
    if dir == 1:
      l1.insert(8,l1[0])
      l1.pop(0)
      l2.insert(0,l2[-1])
      l2.pop()
      return 1
    else:
      l1.insert(0,l1[-1])
      l1.pop()
      l2.insert(8,l2[0])
      l2.pop(0)
      return -1

def rotate_2_3(l2,l3,who,dir):
  if who == 2:
    #시계 반시계
    if dir == 1:
      l2.insert(0,l2[-1])
      l2.pop()
      l3.insert(8,l3[0])
      l3.pop(0)
      #3번 톱니의 회전방향
      return -1
    #반시계 시계
    else:
      l2.insert(8,l2[0])
      l2.pop(0)
      l3.insert(0,l3[-1])
      l3.pop()
      return 1
  #반시계 시계  
  else:
    if dir == 1:
      l2.insert(8,l2[0])
      l2.pop(0)
      l3.insert(0,l3[-1])
      l3.pop()
      return 1
    else:
      l2.insert(0,l2[-1])
      l2.pop()
      l3.insert(8,l3[0])
      l3.pop(0)
      return -1

def rotate_3_4(l3,l4,who,dir):
  if who == 3:
    #시계 반시계
    if dir == 1:
      l3.insert(0,l3[-1])
      l3.pop()
      l4.insert(8,l4[0])
      l4.pop(0)
      #4번 톱니의 회전방향
      return -1
    #반시계 시계
    else:
      l3.insert(8,l3[0])
      l3.pop(0)
      l4.insert(0,l4[-1])
      l4.pop()
      return 1
  #반시계 시계  
  else:
    if dir == 1:
      l3.insert(8,l3[0])
      l3.pop(0)
      l4.insert(0,l4[-1])
      l4.pop()
      return 1
    else:
      l3.insert(0,l3[-1])
      l3.pop()
      l4.insert(8,l4[0])
      l4.pop(0)
      return -1

bin = [0,0,0,0,0,0,0,0]
for _ in range(n):
  li1 = copy.deepcopy(l1)
  li2 = copy.deepcopy(l2)
  li3 = copy.deepcopy(l3)
  li4 = copy.deepcopy(l4)
  a, b = map(int,input().split())
  if a == 1:
    if li1[2] == li2[6]:
      rotate_1_2(l1,bin,a,b)
      continue
    else:
      b = rotate_1_2(l1,l2,a,b)
      if li2[2] == li3[6]:
        continue
      else:
        b = rotate_2_3(bin,l3,2,b)
        if li3[2] == li4[6]:
          continue
        else:
          rotate_3_4(bin,l4,3,b)
  elif a== 2:
    l2copy = copy.deepcopy(l2)
    if li1[2] == li2[6] and li2[2] == li3[6]:
      rotate_1_2(bin,l2,a,b)
      continue
    if li1[2] != li2[6]:
      rotate_1_2(l1,l2copy,a,b)
    if li2[2] == li3[6]:
        l2 = l2copy
        continue
    else:
      b = rotate_2_3(l2,l3,2,b)
      if li3[2] == li4[6]:
        continue
      else:
        rotate_3_4(bin,l4,3,b)
  elif a== 3:
    l3copy = copy.deepcopy(l3)
    if li3[2] == li4[6] and li2[2] == li3[6]:
      rotate_2_3(bin,l3,a,b)
      continue
    if li3[2] != li4[6]:
      rotate_3_4(l3copy,l4,a,b)
    if li2[2] == li3[6]:
      l3 = l3copy
      continue
    else:
      b = rotate_2_3(l2,l3,3,b)
      if li1[2] == li2[6]:
        continue
      else:
        rotate_1_2(l1,bin,2,-b)
  elif a== 4:
    if li3[2] == li4[6]:
      rotate_3_4(bin,l4,a,b)
      continue
    else:
      b = rotate_3_4(l3,l4,a,b)
      if li2[2] == li3[6]:
        continue
      else:
        b = rotate_2_3(l2,bin,3,-b)
        if li1[2] == li2[6]:
          continue
        else:
          rotate_1_2(l1,bin,2,-b)

print(l1[0] + 2*l2[0]+ 4*l3[0] + 8*l4[0])