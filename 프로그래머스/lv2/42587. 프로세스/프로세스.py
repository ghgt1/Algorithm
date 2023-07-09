from collections import deque
def solution(priorities, location):
    answer = 0
    tmp = []
    for k in range(len(priorities)):
        tmp.append([priorities[k],k])
    queue = deque(tmp)
    l1 = []
    while len(queue) !=0:
        a = queue.popleft()
        tmp = []
        for k in queue:
            tmp.append(k[0])
        if len(queue) != 0 and max(tmp) > a[0]:
            queue.append(a)
        else:
            l1.append(a)
#     일단 실행순서 배열을 만들자
    for k in range(len(l1)):
        if l1[k][1] == location:
            answer = k+1
            return answer
    return answer