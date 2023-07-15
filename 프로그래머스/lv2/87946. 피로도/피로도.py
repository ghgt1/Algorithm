from itertools import permutations
def solution(stat, dungeons):
    res = []
    per = list(permutations(dungeons,len(dungeons)))
    
#     다돌려봤자 8!
    for k in per:
        a = stat
        total = 0
        for u in k:
            if a>=u[0]:
                total+=1
                a-=u[1]
            else:
                continue
        res.append(total)
    answer = max(res)
    return answer