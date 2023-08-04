def solution(s):
    answer = len(s)
#     맨앞에서 잘라야한다는게 함정
    for i in range(1, len(s) // 2 + 1):
        tmp = ""
        count = 1
        length =0
        for u in range(0,len(s)+1,i):
            if s[u:u+i] == tmp:
                count+=1
            else:
                length +=len(s[u:u+i])
                if count>=2:
#                     숫자길이더하기
                    length += len(str(count))
                count = 1
                tmp = s[u:u+i]
        answer = min(answer,length)
    return answer