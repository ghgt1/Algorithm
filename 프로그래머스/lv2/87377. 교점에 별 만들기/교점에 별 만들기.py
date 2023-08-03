def solution(line):
    answer = []
    candidates=[]
    #1000제곱 즉 전체 쌍을 다 보는거임
    def cross(a,b,e,c,d,f):
        if a*d == b*c:
            return -1
        cal = (((b*f-e*d))/((a*d-b*c)), ((e*c-a*f)/(a*d-b*c)))
        if cal[0] == int(cal[0]) and cal[1] == int(cal[1]):
            return [int(cal[0]),int(cal[1])]
        else:
            return -1
    for k in range(len(line)):
        for u in range(len(line)):
            if k == u:
                continue
            tmp = cross(line[k][0],line[k][1],line[k][2],line[u][0],line[u][1],line[u][2])
            if tmp !=-1:
                candidates.append(tmp)
    #x,y최대 최소 차이로 컨테이너 만들기
    a = []
    b = []
    for k in candidates:
        c,d = k
        a.append(c)
        b.append(d)
    width = max(a) - min(a) +1
    height = max(b) - min(b) +1
    #로컬라이즈만큼 빼면됨 좌표를
    width_localize = min(a)
    height_localize = max(b)
    answer = [['.' for _ in range(width)] for _ in range(height)]
    for k in candidates:
        x,y = k
        answer[height_localize-y][x-width_localize] = '*'
    graph = []
    for k in answer:
        graph.append(''.join(k))
    return graph