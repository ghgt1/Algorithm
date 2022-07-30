import sys
class Trie:
  def __init__(self):
    self.root = {} #초기화. 하나의 트라이가 dic으로 구성
#각단어는 dic속의 dic처럼 구성됨.
def insert(self, a):
  current_node = self.root
  for k in a:
    if k not in current_node: #현재 트라이에 해당 접두사가 없으면 새로만듬
      current_node[k] = {}
    current_node = current_node[k]

def search(self, a):
  current_node = self.root
  for k in a:
    if k in current_node:
      current_node = current_node[k]#계속 찾아라
    else:
      return False
  if len(current_node) != 0:
    return True
  else:
    return False

t = int(input())
for _ in range(t):
  trie = Trie()
  n = int(input())
  l1 = []
  for k in range(n):
    tmp = sys.stdin.readline().rstrip()
    insert(trie,tmp)
    l1.append(tmp)
  flag = True
  for k in l1:
    count = 0
    if search(trie,k):
      flag = False
      break
    else:
      continue
  if flag:
    print("YES")
  else:
    print("NO")
