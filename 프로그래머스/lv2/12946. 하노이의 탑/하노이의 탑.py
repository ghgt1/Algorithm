def solution(n):
    answer = []
    #사실 개수점화식은 f(n) + 1 + f(n)
    # n개일때
    # n-1개를 3번거쳐 2번으로 보내야함. 
    # 1개를 3번으로 보냄
    # n-1개를 1번거쳐 3번으로 보내야함.
    def hanoi(n,start,mid,end):
        if n == 1:
            return answer.append([start,end])
        hanoi(n-1,start,end,mid)
        answer.append([start,end])
        hanoi(n-1,mid,start,end)
    
    hanoi(n,1,2,3)
    return answer