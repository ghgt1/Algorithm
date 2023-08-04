def solution(s):
    answer = ''
    result = []
    index = 0
    for k in range(len(s)):
        if s[k] == ' ':
            index = 0
            result.append(' ')
            continue
        if index%2==0:
            result.append(s[k].upper())
        else:
            result.append(s[k].lower())
        index+=1
    answer = ''.join(result)
        
    return answer