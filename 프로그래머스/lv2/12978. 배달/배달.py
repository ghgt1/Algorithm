import heapq
INF = int(1e9)
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    for k in road:
        a,b,c = k
        graph[a].append((b,c))
        graph[b].append((a,c))
    distance = [INF]*(N+1)
    def dijkstra(start):
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
    dijkstra(1)
    for u in distance:
        if u <= K:
            answer+=1

    return answer