from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_gap = -1
    #어차피 여러발맞춰도, k점만큼만 가져가니... 그리디하게 생각해야할듯
    #중복조합으로 11개의 과녁중에서 n개만큼 뽑으면됨.
    
    l1 = [i for i in range(11)]
    
    candidates = list(combinations_with_replacement(l1,n))
    
    for k in candidates:
        lion = [0 for i in range(11)]
        for u in k:
            lion[u] +=1
        lion.reverse()
        #이제 info와 lion완성
        a = 0
        b = 0
        for u in range(11):
            if info[u] ==0 and lion[u] ==0:
                continue
            #어피치승
            if info[u] >= lion[u]:
                a+=(10-u)
            else:
                b+=(10-u)
        if b>a and max_gap<(b-a):
            max_gap = b-a
            answer = lion
    
    return answer