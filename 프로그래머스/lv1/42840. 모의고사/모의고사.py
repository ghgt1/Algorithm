from collections import deque
def solution(answers):
    answer = []
    # answers 길이 만큼 찍는 답을 만들어두자
    l1 = []
    l2 = []
    l3 = []
    queue = deque([1,3,4,5])
    queue2 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    for k in range(0,len(answers)):
        l1.append(k%5 + 1)
        
    for k in range(0,len(answers)):
        if k%2 == 0:
            l2.append(2)
        else:
            # 1(1), 3(3), 4(5), 5(7)
            tmp = queue.popleft()
            l2.append(tmp)
            queue.append(tmp)
    
    for k in range(len(answers)):
            tmp = queue2.popleft()
            l3.append(tmp)
            queue2.append(tmp)
    a = 0
    b = 0
    c = 0
    for k in range(len(answers)):
        if l1[k] == answers[k]:
            a+=1
        if l2[k] == answers[k]:
            b+=1
        if l3[k] == answers[k]:
            c+=1
    big = max(a,b,c)
    if a == big:
        answer.append(1)
    if b == big:
        answer.append(2)
    if c == big:
        answer.append(3)
    return answer