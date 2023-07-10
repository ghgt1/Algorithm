def solution(sizes):
    # 모든 가로 세로를 시도해보자.
    # 아니지 가로든 세로든 최댓값중 하나는 size의 최대값이 될거임
    tmp = []
    for k in sizes:
        a,b = k
        tmp.append(a)
        tmp.append(b)
    big = max(tmp)
    l1 = []
    for k in range(1,1001):
            l1.append([k,big])
    res = []
    for k in l1:
        a,b = k
        flag = True
        for u in sizes:
            c,d = u
            if (a>=c and b>=d) or (a>=d and b>=c):
                continue
            else:
                flag = False
        if flag:
            res.append(a*b)
    answer = min(res)
    return answer