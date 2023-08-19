import sys
sys.setrecursionlimit(10**6)

def solution(n):
    answer = 0
    dic = {}
    dic[0] = 0
    dic[1] = 1
    dic[2] = 1
    def fibo(num):
        if num in dic:
            return dic[num]
        else:
            dic[num] = fibo(num-1) + fibo(num-2)
            return dic[num]
    answer = fibo(n)
    return answer%1234567