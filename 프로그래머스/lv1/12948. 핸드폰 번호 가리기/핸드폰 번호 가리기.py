def solution(phone_number):
    answer = ''
    l1 = []
    for k in phone_number:
        l1.append(k)
    for k in range(len(l1)-4):
        l1[k]='*'
    answer = ''.join(l1)
    return answer