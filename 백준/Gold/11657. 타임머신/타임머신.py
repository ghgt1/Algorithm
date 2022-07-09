n, m = map(int,input().split())
INF = int(1e9)
# 간선의개수가 10000개이하이고, 음의간선이 포함되므로 벨만-포드 사용
graph = []
distance = [INF] * (n+1)
#벨만포드는 visited필요없고 graph를 순차적으로 모든 edge를 확인하므로 노드 인접리스트를 만들필요없음.
for _ in range(m):
  a,b,c = map(int,input().split())
  graph.append((a,b,c))
#시작점은 1번노드
distance[1] = 0
def belman_ford():
  #자 이론적으로 벨만포드는 n-1번 탐색. 그러나 순환을 확인해야하므로 한번더해준다
  for u in range(n):
    for k in range(m):
      current_node, next_node, cost = graph[k]
      #distance[current_node]!=INF는 우리가 현재 도달할수있는 정점인지 아닌지를 알려주므로 필수적이다. INF이면 보면 안되는 간선인것.
      if distance[current_node]!=INF and distance[next_node] > distance[current_node] + cost:
        distance[next_node] = distance[current_node] + cost
        if u== n-1: #이게 순환체크 경우
          return True
  return False

if belman_ford():
  print(-1)
else:
  for u in range(n-1):
    if distance[u+2] != INF:
      print(distance[u+2])
    else:
      print(-1)

          