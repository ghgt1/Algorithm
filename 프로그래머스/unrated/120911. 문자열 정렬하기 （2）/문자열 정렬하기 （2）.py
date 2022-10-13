def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    answer = my_string
    l1 = list(map(str,answer))
    l1.sort()
    answer = ''
    for k in l1:
        answer = answer + k
    return answer