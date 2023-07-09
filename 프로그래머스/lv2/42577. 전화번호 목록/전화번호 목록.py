def solution(phone_book):
    answer = True
#     20  * 100만
    dic = {}
    for k in phone_book:
        dic[k] = 1
    for k in phone_book:
        for u in range(1, len(k)):
            if k[:u] in dic:
                return False
    return answer