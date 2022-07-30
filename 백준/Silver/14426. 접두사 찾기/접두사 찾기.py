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
  return True

trie = Trie()
n,m = map(int,input().split())
for _ in range(n):
  insert(trie,input())
count = 0
for _ in range(m):
  if search(trie,input()):
    count=count+1
print(count)