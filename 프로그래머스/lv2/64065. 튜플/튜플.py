def solution(s):
    answer = []
    def sort_by(data):
        return data[1]
    #개수별로 정렬해야함
    #정렬된거에서 어떤 원소가 늘어나는지 파악하면끝
    l1 = s.split('},')
    l2 = []
    for k in l1:
        k = k.replace('{','')
        k = k.replace('}','')
        tmp = k.split(',')
        l2.append((tmp,len(tmp)))
    result = sorted(l2,key=sort_by)
    dic={}
    for k in result:
        l1, a = k
        for u in l1:
            if u in dic:
                continue
            else:
                dic[u] = 1
                answer.append(int(u))
    return answer