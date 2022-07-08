import heapq
import sys
n = int(input())
heap = []
tmp = list(map(int,sys.stdin.readline().split()))
#처음에 다 때려놓고 최대힙으로 n개 꺼냈는데 그러면 메모리가 터짐
#따라서 최소힙으로 heap안에는 n개이상의 원소가 안들어가게 관리함
#n개이상되면 작은것들 빼버림
for u in tmp:
  heapq.heappush(heap,u)
for k in range(n-1):
  tmp = list(map(int,sys.stdin.readline().split()))
  for u in tmp:
    heapq.heappush(heap,u)
  for _ in range(n):
    heapq.heappop(heap)
print(heapq.heappop(heap))