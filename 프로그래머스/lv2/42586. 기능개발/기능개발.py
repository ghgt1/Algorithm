from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    
    #결국 앞에서부터가 중요
    #큐사용
    queue = deque(progresses)
    #카운트는 한번에 몇개 배포
    count = 0
    index = 0
    while queue:
        count = 1
        a = queue.popleft()
        time = math.ceil((100-a)/speeds[index])
        index+=1
        for k in range(len(queue)):
            queue[k] += (speeds[index+k] * time)
        while queue and queue[0] >= 100:
            queue.popleft()
            index+=1
            count+=1
        answer.append(count)
    return answer