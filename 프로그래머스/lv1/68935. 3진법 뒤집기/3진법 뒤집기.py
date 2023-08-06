def solution(n):
    answer = 0
#     몫과 나머지 쓰면됨
    result = []
    while n>0:
        n,q = divmod(n,3)
        result.append(str(q))
    answer = ''.join(result)
    answer = int(answer,3)
    return answer