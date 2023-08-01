def solution(routes):
    answer = 1
    routes.sort()
    stack = [routes[0][1]]

    print(routes)
    for k in range(1,len(routes)):
        end = stack.pop()
        a, b= routes[k]
        #겹쳐
        if a <= end:
            stack.append(min(end,b))
        #안겹쳐
        else:
            answer+=1
            stack.append(b)
    
    print(stack)
    return answer