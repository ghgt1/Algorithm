def solution(record):
    answer = []
    dic={}
    for k in record:
        l1 = k.split(' ')
        if l1[0] == 'Enter':
            dic[l1[1]] = l1[2]
        elif l1[0] == 'Change':
            dic[l1[1]] = l1[2]
    for k in record:
        l1 = k.split(' ')
        if l1[0] == 'Enter':
            answer.append(dic[l1[1]] +"님이 들어왔습니다.")
        elif l1[0] == 'Leave':
            answer.append(dic[l1[1]] +"님이 나갔습니다.")
    return answer