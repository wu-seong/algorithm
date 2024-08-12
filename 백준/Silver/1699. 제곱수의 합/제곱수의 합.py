import sys
import math
input = sys.stdin.readline

N = int(input().rstrip())

dp = [100000] * (N+1)
dp[1] = 1
for i in range(2,N+1):
    f_sqrt = math.sqrt(i)
    if f_sqrt.is_integer():
        dp[i] = 1
    else:
        f_sqrt = int(f_sqrt//1)
        # 여러 제곱 수를 비교
        for j in range(f_sqrt//2, f_sqrt+1):
            dp[i] = min(dp[i], dp[(j**2)] + dp[i-(j**2)])
print(dp[N])

# 루트 한것 + 나머지?