def solution(places):
    answer = []
    #거리2까지만 보자
    #후보군은 12개, 그중에서 맨해튼거리가 1인애들은 어쩔수없음. 안되는거임
    #맨해튼거리가 2인애들은 경우에따라 막혀있을수도있음
    #상하로 거리2
    dx1=[-2,2,0,0]
    dy1=[0,0,-2,2]
    #대각으로 거리2
    dx2=[-1,-1,1,1]
    dy2=[1,-1,1,-1]
    #거리1
    dx3=[-1,1,0,0]
    dy3=[0,0,-1,1]
    
    for i in places:
        graph = i
        coordinates = []
        flag = True
        for k in range(5):
            for u in range(5):
                if graph[k][u] == 'P':
                    coordinates.append((k,u))
        for k in coordinates:
            x,y = k
            for u in range(4):
                nx = x+dx1[u]
                ny = y+dy1[u]
                if nx<0 or ny<0 or nx>=5 or ny>=5:
                    continue
                if graph[nx][ny] == 'P':
                    if graph[int((x+nx)/2)][int((y+ny)/2)] == 'X':
                        continue
                    else:
                        flag = False
                        break
            if not flag:
                break
                        
            for u in range(4):
                nx = x+dx2[u]
                ny = y+dy2[u]
                if nx<0 or ny<0 or nx>=5 or ny>=5:
                    continue
                if graph[nx][ny] == 'P':
                    if graph[nx][y] and graph[x][ny] == 'X':
                        continue
                    else:
                        flag = False
                        break
                        
            if not flag:
                break
            
            for u in range(4):
                nx = x+dx3[u]
                ny = y+dy3[u]
                if nx<0 or ny<0 or nx>=5 or ny>=5:
                    continue
                if graph[nx][ny] == 'P':
                    flag = False
                    break
                        
            if not flag:
                break
                
        if flag:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer