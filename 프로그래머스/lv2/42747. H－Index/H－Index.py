def solution(citations):
    answer = 0
    cite = 100000
    while cite>0:
        count = 0
        for k in citations:
            if k>=cite:
                count +=1
        if count>=cite:
            return cite
        else:
            cite-=1
    return answer