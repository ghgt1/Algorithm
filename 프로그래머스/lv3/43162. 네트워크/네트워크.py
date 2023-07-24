def solution(n, computers):
    answer = 0
    # 인접행렬 to 인접 리스트
    graph = [[] for _ in range(n)]
    for k in range(n):
        for u in range(n):
            if computers[k][u] == 1:
                if u not in graph[k]:
                    graph[k].append(u)
                if k not in graph[u]:
                    graph[u].append(k)
    print(graph)

        
    def DFS(v,visited):
        visited[v] = True
        for u in graph[v]:
            if visited[u] == False:
                DFS(u,visited)

    res = []
    for k in range(n):
        visited = [False] * n
        DFS(k,visited)
        if visited in res:
            continue
        res.append(visited)
        
    return len(res)