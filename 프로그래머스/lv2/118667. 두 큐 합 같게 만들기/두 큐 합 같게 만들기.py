from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1  = sum(queue1)
    sum2 = sum(queue2)
    length = len(queue1)
    
    while sum1 != sum2:
        answer+=1
        if answer> 3*length:
            answer = -1
            break
        if sum1>sum2:
            queue2.append(queue1.popleft())
            sum2+=queue2[-1]
            sum1-=queue2[-1]
        elif sum1 < sum2:
            queue1.append(queue2.popleft())
            sum1+=queue1[-1]
            sum2-=queue1[-1]
        else:
            break
    return answer