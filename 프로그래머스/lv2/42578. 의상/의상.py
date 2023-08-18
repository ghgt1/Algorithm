def solution(clothes):
    answer = 0
    dic = {}
    for k in clothes:
        a,b = k
        if b not in dic:
            dic[b] = [a]
        else:
            dic[b].append(a)
    tmp = 1
    for k in dic:
        tmp*=len(dic[k])+1
    answer = tmp-1
    return answer