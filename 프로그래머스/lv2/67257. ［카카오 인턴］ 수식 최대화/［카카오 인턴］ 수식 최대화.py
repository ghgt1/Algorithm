from copy import deepcopy
from itertools import permutations
def solution(expression):
    result = []
    answer = 0
    #permutation으로 순서 정해야함.
    #stack에 쌓으면서 순회. 하나의 연산자마다. 괜찮은듯?
    #일단 연산자 후보군 정하자
    l1 = []
    for k in expression:
        if not k.isdigit():
            l1.append(k)
    l1 = list(set(l1))
    l2 = list(permutations(l1,len(l1)))
    stack = []
    
    
    #일단 해당 문자열을 스플릿해야하는데...
    tmp = ""
    expressions = []
    for k in expression:
        if k in l1:
            expressions.append(int(tmp))
            expressions.append(k)
            tmp = ""
        else:
            tmp +=k
    expressions.append(int(tmp))
    
    storedExpressions = deepcopy(expressions)
    
    for k in l2:
        expressions = storedExpressions
        for u in k:
            for q in range(len(expressions)):
                if q == 0:
                    stack.append(expressions[q])
                    continue
                if q>=1 and expressions[q-1] == u:
                    if u == '-':
                        stack.pop()
                        stack.append(stack.pop() - expressions[q])
                    elif u == '+':
                        stack.pop()
                        stack.append(stack.pop() + expressions[q])
                    elif u == '*':
                        stack.pop()
                        stack.append(stack.pop() * expressions[q])
                    continue
                stack.append(expressions[q])
            expressions = stack
            stack = []
        result.append(abs(expressions[-1]))
    return max(result)