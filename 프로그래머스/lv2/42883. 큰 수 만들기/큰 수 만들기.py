def solution(number, u):
    answer = ''
    stack = [number[0]]
    for k in range(1, len(number)):
        while stack and stack[-1] < number[k] and u>0:
            stack.pop()
            u-=1
        stack.append(number[k])
    while u!=0:
        stack.pop()
        u-=1
    answer = str(int(''.join(stack)))
    return answer