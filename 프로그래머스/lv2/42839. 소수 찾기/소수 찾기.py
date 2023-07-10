from itertools import permutations
import math

def is_prime_number(num):
    if num == 1 or num == 0:
        return False
    flag = True
    for k in range(2,int(math.sqrt(num))+1):
        if num%k == 0:
            return False
    return flag

def solution(numbers):
    # 소수 판단 알고리즘
    # permutation으로 모든 순열 갖고있자
    l1 = []
    res = []
    for k in numbers:
        l1.append(k)
    for k in range(1,len(numbers)+1):
        tmp = list(permutations(l1,k))
        for k in tmp:
            a = ""
            for u in k:
                a+=u
            if is_prime_number(int(a)):
                res.append(int(a))

    answer = len(list(set(res)))
    return answer