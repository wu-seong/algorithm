import sys

input = sys.stdin.readline

N = int(input().rstrip())
seq = list(map(int, input().rstrip().split()))

# 새로운 원소가 추가되면
# 원소값이 각 부분 수열의 마지막 원소보다 작다면 해당 원소를 수열에 추가하여 길이를 갱신
dp = [1] * N
max_length = 1
for i in range(1,N):
    # 새로 만들어진 여러 수열 중 가장 긴 길이로 갱신
    for j in range(i):
        # 새로운 원소가 더 작다면 수열에 추가
        if seq[j] > seq[i]:
            dp[i] = max(dp[i], dp[j]+1)
    max_length = max(max_length, dp[i])
print(max_length)
