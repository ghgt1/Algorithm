def solution(m, n, puddles):
    # 오른쪽과 아래로만 이동하므로, dp[x+1][y+1] = dp[x][y+1] + dp[x+1][y]
    answer = 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    for k in puddles:
        a,b = k
        dp[b][a] = -1
    print(dp)
    for k in range(1,n+1):
        for u in range(1,m+1):
            if dp[k][u] == -1:
                continue
            dp[1][1] = 1
            if dp[k-1][u] == -1:
                if dp[k][u-1] == -1:
                    continue
                else:
                    dp[k][u] = dp[k][u-1]
            else:
                if dp[k][u-1] == -1:
                    dp[k][u] = dp[k-1][u]
                else:
                    dp[k][u] = dp[k-1][u] + dp[k][u-1]
    return dp[-1][-1] % 1000000007