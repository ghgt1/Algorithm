import sys
sys.setrecursionlimit(10**6)

def solution(n, times):
    global answer
    #소모시간+남은시간을 합쳐서 비교해야함
    #중요한건 심사관
    #멍청한놈. 그냥 최소시간이 필요하니. 시간을 매개변수로 찾자
    answer = float('inf')
    time = n * max(times)
    
    def check_ok(candidate):
        tmp = 0
        for k in times:
            tmp += candidate//k
        if tmp>=n:
            return True
        else:
            return False
    
    def parametric_search(start,end):
        global answer
        #이시간이 들어왔을때 되는지 판단
        mid = (start+end)//2
        if start>=end:
            return
        if check_ok(mid):
            end = mid 
            parametric_search(start,end)
            answer = min(answer,mid)
        else:
            start = mid+1
            parametric_search(start,end)
            
    parametric_search(0,time)
    return answer