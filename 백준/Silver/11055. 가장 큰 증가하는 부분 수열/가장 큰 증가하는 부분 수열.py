import sys
input = sys.stdin.readline

# 이전의 정답에 고정되어 이와 점화식을 연게 시키는거에 시야가 좁아지지 말자
# 원소가 추가 되었을 때 그 원소가 지금 까지 구한 부분 수열(부분 문제)초에 추가될 수 있는지가 핵심

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

dp = [0] * N
for i in range(N):
    dp[i] = A[i]
max_sum = dp[0]
for i in range(1,N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + A[i],dp[i])
    max_sum = max(max_sum,dp[i])

print(max_sum)