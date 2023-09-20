def solution(numbers, target):
    global answer
    answer = 0
    l1 = []
    def DFS():
        global answer
        if len(numbers) == len(l1):
            if sum(l1) == target:
                answer+=1
                return
            else:
                return
        l1.append(numbers[len(l1)])
        DFS()
        l1.pop()
        l1.append(-numbers[len(l1)])
        DFS()
        l1.pop()
    DFS()
    return answer