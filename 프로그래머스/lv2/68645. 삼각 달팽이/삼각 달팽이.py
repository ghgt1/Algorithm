def solution(n):
    answer = []
    graph = [[0]*n for _ in range(n)]
    dx = [1,0,-1]
    dy = [0,1,-1]
    num = 1
    x = 0
    y = 0
    #angle/3의 나머지에 따라 dx dy결정
    angle = 0
    end = int((n*(n+1))/2)
    
    l1 = [k for k in range(n,0,-1)]
    l2 = [n]
    for k in range(1,len(l1)):
        l2.append(l2[k-1]+l1[k])
        
    index = 0
    
    for k in range(end):
        graph[x][y] = num
        if num==end:
            break
        num+=1
        
        x = x+dx[angle%3]
        y = y+dy[angle%3]
        
        #앵글 바꾸기

        if num == l2[index]:
            index+=1
            angle+=1
            
    for k in graph:
        for u in k:
            if u ==0:
                break
            answer.append(u)
    return answer