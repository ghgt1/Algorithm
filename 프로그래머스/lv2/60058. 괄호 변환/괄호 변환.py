def solution(p):
    answer = ''
    def check_alright(data):
        stack = []
        for k in data:
            if k == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    stack.append(k)
            else:
                stack.append(k)
        if len(stack)==0:
            return True
        else:
            return False
        
    def make_alright(data):
        if len(data) == 0:
            return data
        l1 = []
        l2 = []
        for k in range(2,len(data)+1,2):
            l1 = data[:k]
            l2 = data[k:]
            if l1.count('(') == l1.count(')'):
                break
        if check_alright(l1):
            return l1 + make_alright(l2)
        else:
            l1.pop(0)
            l1.pop()
            for u in range(len(l1)):
                if l1[u] == '(':
                    l1[u] = ')'
                else:
                    l1[u] = '('
            return ['('] + make_alright(l2) + [')'] + l1
    
    #u는 가장 작은 균형잡힌 괄호 문자열
    if check_alright(p):
        return p
    else:
        answer = make_alright(list(p))
        answer = ''.join(answer)
        
    return answer