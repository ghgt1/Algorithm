a = input()
b = input()
#LCS 알고리즘 사용. 최대 1000글자
dp = [[0 for _ in range(1001)] for _ in range(1001)]
for i in range(len(a)):
  for j in range(len(b)):
    if i==0 and j==0:
      if a[i] != b[j]:
        dp[i][j] = 0
      else:
        dp[i][j] = 1
    elif a[i] == b[j]:
      dp[i][j] = dp[i-1][j-1] + 1
    elif a[i] != b[j]:
      dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[len(a)-1][len(b)-1])