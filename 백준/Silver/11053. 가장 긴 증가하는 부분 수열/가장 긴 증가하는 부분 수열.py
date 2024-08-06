import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
dp = [1] * N

max_length = 1
for i in range(1,N):
    for j in range(i):
        # 더 큰 숫자가 오면 수열에 추가 및 길이 계산
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
    max_length = max(max_length, dp[i])
print(max_length)