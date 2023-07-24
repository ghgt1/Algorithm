from collections import deque

def solution(maps):
    answer = 0
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    # visited관리는 안해도 되고, 종료조건만 설정. BFS
    def BFS(x,y):
        queue = deque([])
        queue.append((x,y))
        while queue:
            x, y = queue.popleft()
            for q in range(4):
                nx = x+dx[q]
                ny = y+dy[q]
                if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]):
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] +1
                    queue.append((nx,ny))
                    if nx == len(maps) and ny == len(maps[0]):
                        return maps[nx][ny]
    BFS(0,0)
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
    return answer