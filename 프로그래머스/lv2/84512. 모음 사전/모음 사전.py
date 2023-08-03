from itertools import combinations

def solution(word):
    answer = 0
    mo = ['A','E','I','O','U']*5
    l1 = []
    for k in range(1,6):
        candidates = list(combinations(mo,k))
        for k in candidates:
            a = ''.join(k)
            l1.append(a)
    l1 = list(set(l1))
    l1.sort()
    answer = l1.index(word)+1
    return answer