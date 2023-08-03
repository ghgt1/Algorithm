def solution(rows, columns, queries):
    answer = []
    start = 1
    graph = []
    for u in range(1,rows+1):
        tmp = []
        for k in range(1,columns+1):
            tmp.append(start)
            start+=1
        graph.append(tmp)
    for k in queries:
        #인덱스들만 먼저 뽑자
        candidates = []
        x1,y1,x2,y2 = k
        for u in range(y2-y1+1):
            candidates.append((x1-1,u+y1-1))
            
        for u in range(x2-x1):
            candidates.append((x1+u,y2-1))
            
        for u in range(y2-y1):
            candidates.append((x2-1,y2-2-u))
        
        for u in range(x2-x1-1):
            candidates.append((x2-u-2,y1-1))

        candidates2 = []
        for u in candidates:
            a,b = u
            candidates2.append(graph[a][b])
        
        for u in range(len(candidates)):
            a,b = candidates[u]
            graph[a][b] = candidates2[u-1]
        
        answer.append(min(candidates2))
            
    return answer