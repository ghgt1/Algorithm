from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    result = []
    #개수들 서로 곱해주면됨.
    #개수얼마안되니 완탐 돌리자
    #우선 일치하는지 확인하는 함수 필요
    def is_mapped(a,b):
        if len(a) != len(b):
            return False
        flag = True
        for k in range(len(a)):
            if a[k] == b[k] or b[k] == '*':
                continue
            else:
                return False
        return flag
    
    l1 = list(permutations(user_id,len(banned_id)))
    
    for k in range(len(l1)):
        flag = True
        for u in range(len(banned_id)):
            if is_mapped(l1[k][u],banned_id[u]):
                continue
            else:
                flag=False
                break
        if flag:
            tmp = list(l1[k])
            tmp.sort()
            if tmp not in result:
                result.append(tmp)
    #조합뽑으면됨
    return len(result)