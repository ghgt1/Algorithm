n = input()
dic = {}
#거꾸로 dp로 풀어나간다
if "00" in n or len(n) == 0:
  print(0)
elif n[0] == '0':
  print(0)
else:
  for k in range(len(n)):
    tmp = n[-k-1:]
    if len(tmp)>=3:
      if int(tmp[0:2]) == 10 or int(tmp[0:2]) == 20:
        dic[tmp] = dic[tmp[2:]]
      elif 10<int(tmp[0:2])<=26:
        if tmp[2] == '0':
          dic[tmp] = dic[tmp[1:]]
        else:
          dic[tmp] = dic[tmp[1:]] + dic[tmp[2:]]
      elif int(tmp[0:2])>26:
        if tmp[1] == '0':
          dic[n] = 0
          break
          dic[tmp] = dic[tmp[2:]]
        else:
          dic[tmp] = dic[tmp[1:]]
      elif tmp[0] == '0':
        continue
    elif len(tmp) == 2:
      if int(tmp) == 10 or int(tmp) == 20:
        dic[tmp] = 1
      elif 10<int(tmp)<=26:
        dic[tmp] = 2
      else:
        dic[tmp] = dic[tmp[1:]]
    else:
      if int(tmp)!=0:
        dic[tmp] = 1
      else:
        dic[tmp]=0
  print(dic[n] % 1000000)