def solution(n, number):
    answer = -1
    
    dp = [[] for _ in range(9)]
    dp[1] = [n]
    dp[2] = [11*n, 2*n,0,1,n*n]
    for k in range(3,9):
        tmp = [int('1'*k)*n]
        for u in range(1,k):
            for a in dp[u]:
                for b in dp[k-u]:
                    tmp.append(a+b)
                    tmp.append(a-b)
                    tmp.append(a*b)
                    if b!=0:
                        tmp.append(a/b)
        dp[k] = tmp
    for k in range(1,9):
        if number in dp[k]:
            return k
    return answer