import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
P = list(map(int, input().rstrip().split()))
# 4
# 1 5 6 7

dp = [0 for _ in range(N+1)]
dp[1] = P[0]

# 순차적으로 최댓값 구하기
for i in range(2, N+1):
    # 40 31 22, 02 11   2 -> 1 3 -> 1 4 -> 2  5 -> 2
    max = P[i-1]
    for j in range(1, (i//2)+1):
        sum = dp[j] + dp[i-j]
        if sum > max:
            max = sum
    dp[i] = max      

print("%d\n"%dp[N])