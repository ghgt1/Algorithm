def solution(n, lost, reserve):
    answer = 0
    l1 = [1 for _ in range(n+2)]
    for k in lost:
        l1[k] -=1
    for k in reserve:
        l1[k] +=1
    print(l1)
    for k in range(1,len(l1)):
        if l1[k] == 0 and l1[k-1] ==2:
            l1[k] =1
            l1[k-1] = 1
        elif l1[k] ==0 and l1[k+1] == 2:
            l1[k] = 1
            l1[k+1] = 1
    for k in l1:
        if k>=1:
            answer+=1
            
    answer -=2

    
    return answer