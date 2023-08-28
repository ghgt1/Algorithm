from collections import deque

def solution(maps):
    answer = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    def bfs(graph,visited):
        queue = deque([(0,0)])
        while queue:
            x,y = queue.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]):
                    continue
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
    bfs(maps,visited)
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
    return answer