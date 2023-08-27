import copy
def solution(n, computers):
    graph = [[] for _ in range(n+1)]
    res = []
    for k in range(n):
        for u in range(n):
            if computers[k][u] == 1 and k!=u:
                graph[k].append(u)
    print(graph)
    
    def dfs(graph,v,visited):
        visited[v] = True
        for k in graph[v]:
            if not visited[k]:
                dfs(graph,k,visited)
    
    for k in range(n):
        graph2 = copy.deepcopy(graph)
        visited = [False]*n
        dfs(graph2,k,visited)
        if visited not in res:
            res.append(visited)
    
    return len(res)