def solution(s):
    answer = True
    for k in s:
        if 48<=ord(k)<=57:
            continue
        else:
            answer = False
            break
    if len(s)!=4 and len(s) != 6:
        answer = False
    return answer