def solution(stones, u):
    global answer
    global const_stone
    answer = 0
    #이런것도 명수를 정해두면?
    #3명이라한다면
    #0231002030
    #4명이면
    #0120001020
    left = 0
    right = max(stones)
    
    const_stone = stones[:]
    
    def is_availabe(mid,stones):
        skip = 0
        for k in stones:
            if k<mid:
                skip+=1
                if skip>=u: return False
            else : skip = 0
        return True
    
    def parametric(start,end):
        global answer
        global const_stone
        stones = const_stone[:]
        mid = (start+end)//2
        if start>end:
            return

        # mid-1만큼 전체에서 뺀다
        # tmp = ""
        # for k in range(len(stones)):
        #     stones[k] -= (mid-1)
        #     if stones[k]<0:
        #         stones[k] = 0
        #     stones[k] = str(stones[k])
        # tmp = ''.join(stones)
        #안된다는거임. 그렇다면 명수를 줄여아함
        # if tmp.find('0'*u) != -1:
        #     parametric(start,mid-1)
        # else:
        #     answer = max(answer,mid)
        #     parametric(mid+1,end)
        if is_availabe(mid,stones):
            answer=  max(answer,mid)
            parametric(mid+1,end)
        else:
            parametric(start,mid-1)
    parametric(left,right)
    return answer