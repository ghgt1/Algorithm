def solution(s, n):
    answer = ''
#     아스키. ord, chr
    l1 = []
    for k in s:
        if k == ' ':
            l1.append(' ')
            continue
        #대문자란뜻
        if ord(k)<=90:
            shift = ord(k)+n
            if shift >90:
                shift-=26
        else:
            shift = ord(k)+n
            if shift > 122:
                shift-=26

        l1.append(chr(shift))
    answer = ''.join(l1)
    return answer