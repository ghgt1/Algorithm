def solution(s):
    answer = True
    l1 = []
    for k in s:
        if len(l1) == 0:
            l1.append(k)
            continue
        if k == ')':
            if l1[-1] == '(':
                l1.pop()
                continue
        else:
            l1.append(k)
    if len(l1) != 0:
        answer = False
                

    return answer