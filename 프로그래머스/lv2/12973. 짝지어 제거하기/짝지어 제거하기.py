def solution(s):
    answer = -1
    #닥치고 스택아닌가?
    stack = []
    
    for k in s:
        if len(stack) == 0:
            stack.append(k)
            continue
        if stack[-1] == k:
            stack.pop()
            continue
        else:
            stack.append(k)
    if len(stack) == 0: 
        return 1
    else:
        return 0
    return answer