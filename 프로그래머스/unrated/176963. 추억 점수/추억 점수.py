def solution(name, yearning, photo):
    answer = []
    dic = {}
    for k in range(len(name)):
        dic[name[k]] = yearning[k]
    for k in photo:
        total = 0
        for u in k:
            if u in dic:
                total += dic[u]
        answer.append(total)
    return answer