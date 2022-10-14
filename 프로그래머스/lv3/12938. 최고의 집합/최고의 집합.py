def solution(n, s):
    answer = []
    if s<n:
        answer.append(-1)
    else:
        for _ in range(n):
            answer.append(int(s/n))
        for i in range(s-sum(answer)):
            answer[i]+=1
    answer.sort()
    return answer