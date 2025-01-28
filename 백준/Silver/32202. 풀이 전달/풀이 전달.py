N = int(input())
dp = [0] * N

dp[0] = 3
fromPairs = [0] * N
fromPairs[0] = 2
fromTeachers = [0] * N
fromTeachers[0] = 1
for i in range(1,N):
    fromPairs[i] = dp[i-1] * 2
    fromTeachers[i] = fromPairs[i-1]
    dp[i] = int((fromTeachers[i] + fromPairs[i]) % (1e9+7))
    #print(fromPairs[i], fromTeachers[i], dp[i])
print(dp[N-1])