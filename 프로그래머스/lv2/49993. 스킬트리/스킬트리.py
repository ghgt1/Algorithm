def solution(skill, skill_trees):
    answer = 0
    dic = {}
    for k in range(len(skill)-1):
        dic[skill[k+1]] = skill[k]
        
    for k in skill_trees:
        flag = True
        candidates = {}
        for u in k:
            # 선수조건이 있으면
            if u in dic:
                if dic[u] in candidates:
                    candidates[u] = 1
                    continue
                else:
                    candidates[u] = 1
                    flag = False
                    break
            else:
                candidates[u]=1
        if flag:
            answer+=1
    return answer