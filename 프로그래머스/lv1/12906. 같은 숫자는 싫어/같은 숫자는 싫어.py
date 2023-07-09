def solution(arr):
    answer = []
    for k in arr:
        if len(answer)!=0:
            if answer[-1] == k:
                continue
            else:
                answer.append(k)
        else:
            answer.append(k)
    return answer