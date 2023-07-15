def solution(brown, yellow):
    answer = []
    
    plus = (brown+4)/2
    a = 3
    b = plus-a
    
    while True:
        if (a-2) * (b-2) == yellow:
            answer = [max(a,b), min(a,b)]
            return answer
        else:
            a+=1
            b-=1
    # return answer