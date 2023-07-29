import heapq
INF = int(1e9)

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    
    for k in edge:
        a,b = k
        #a에서 b로가는 비용이 1
        graph[a].append((b,1))
        graph[b].append((a,1))
    # 1번 노드에서 얼마나 떨어져있는지 각각 계산
    # 최단거리를 구해야하므로 다익스트라 사용
    
    # 시작노드1
    def dijkstra(start):
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0
        while q:
            dist,now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost<distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
    dijkstra(1)
    
    big = 0
    for k in distance:
        if k>big and k!=INF:
            big = k

    return distance.count(big)