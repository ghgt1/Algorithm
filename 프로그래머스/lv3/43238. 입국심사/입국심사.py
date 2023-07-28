import bisect

def solution(n, times):
    answer = 0
    # 그리고 27이안되고 28이됨. 왜? 28/7 = 4 나누기 연산을 통해 최적이 계산되버림
    # 파라메트릭으로 접근
    left = 0
    right = max(times) * n
    target = 0
    
    def cal(time):
        count = 0
        for k in times:
            count += time//k
        if count>=n:
            return True
        else:
            return False
        
    while left<=right:
        print(target,left,right)
        if left > right:
            break
        target = (left+right)//2
        if cal(target):
            right = target-1
            answer = target
        else:
            left = target+1
        
    return answer