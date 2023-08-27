def solution(tickets):
    global count
    answer = []
    #아직 갈곳이 남았는데 경로가 끊겼으면 그 방법은 안되는거임
    graph = {}
    for ticket in tickets:
        a,b = ticket
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
    for k in graph:
        graph[k].sort()
    
    #여기서 중요한점은 visited 처리는, 갈때가 없을때 되야한다
    #경로를 찍어야하는 문제는. 경로를 가지고 가면서 넣었다 빼야한다.
    print(graph)
    def dfs(graph,path,answer):
        print(path)
        if path:
            if path[-1] in graph and graph[path[-1]]:
                path.append(graph[path[-1]].pop(0))
            else:
                answer.append(path.pop())
            dfs(graph,path,answer)
                
    
    dfs(graph,["ICN"],answer)
    answer.reverse()
    return answer