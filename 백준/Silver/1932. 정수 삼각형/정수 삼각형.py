import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = [list(map(int,input().rstrip().split())) for _ in range(n) ]


dp = [ [ 0 for j in range(i+1)] for i in range(n)]
#print(array)
#print(dp)

dp[0][0] = array[0][0]

for i in range(1,n):
    dp[i][0] = dp[i-1][0] + array[i][0]
    dp[i][-1] = dp[i-1][-1] + array[i][-1]
    for j in range(1,i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]

max_sum = 0
for sum in dp[n-1]:
    max_sum = max(max_sum, sum)
print(max_sum)

# DP와 탐색문제를 구별하는법

# 누적되는 합을 구해야 한다면 DP

# 경로나 연결요소의 개수, 탐색 level을 알아야 한다면 탐색