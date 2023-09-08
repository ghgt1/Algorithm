def solution(m, n, board):
    answer = 0
    graph = []
    for k in board:
        graph.append(list(k))
    
    while True:
        candidates = []
        count = 0
        for k in range(m-1):
            for u in range(n-1):
                if graph[k][u] == graph[k+1][u] == graph[k][u+1] == graph[k+1][u+1]:
                    if graph[k][u] == '*':
                        continue
                    count+=1
                    candidates.append((k,u))
                    candidates.append((k+1,u))
                    candidates.append((k,u+1))
                    candidates.append((k+1,u+1))
        if count == 0:
            break
        
        for k in candidates:
            a,b = k
            graph[a][b] = '*'
        #내려주기 작업
        for k in range(n):
            temp = []
            temp2 = []
            for u in range(m):
                if graph[u][k] != '*':
                    temp.append(graph[u][k])
                else:
                    temp2.append('*')
            new = temp2 + temp
            for u in range(m):
                graph[u][k] = new[u]
    for k in graph:
        for u in k:
            if u == '*':
                answer+=1
    return answer