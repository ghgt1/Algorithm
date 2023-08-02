def solution(s):
    answer = []
    zero = 0
    count = 0
    while len(s) != 1:
        tmp = s.count('0')
        zero += tmp
        s = str(bin(int(len(s)-tmp))[2:])
        count +=1
    answer = [count,zero]
    return answer