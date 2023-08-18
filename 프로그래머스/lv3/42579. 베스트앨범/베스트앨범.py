def solution(genres, plays):
    answer = []
    l1 = []
    dic = {}
    def sort_key(data):
        return data[1]
    def sort_key_zero(data):
        return data[0]
    for k in range(len(genres)):
        if genres[k] in dic:
            dic[genres[k]].append((plays[k],k))
        else:
            dic[genres[k]] = [(plays[k],k)]
    for k in dic:
        total = 0
        for u in dic[k]:
            total +=u[0]
        l1.append((k,total))
        dic[k] = sorted(dic[k],key=sort_key,reverse=True)
        dic[k] = sorted(dic[k],key=sort_key_zero)
        dic[k].reverse()

    l1 = sorted(l1,key=sort_key,reverse=True)
    for k in l1:
        a,b = k
        total = 0
        for u in dic[a]:
            total+=1
            c,d = u
            answer.append(d)
            if total>=2:
                break
    return answer