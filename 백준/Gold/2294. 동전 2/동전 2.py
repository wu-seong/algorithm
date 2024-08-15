import sys
input = sys.stdin.readline

# 추가한 동전이 10,000을 넘을 때 pass

# 추가한 동전이 k보다 작을 때 -> 이전 ans

# 추가한 동전이 k와 같을 때 -> 1

# 추가한 동전이 k보다 클 때 -> min(dp[i-1][j], dp[coin] + dp[i][j-coin])

# dp[i]
n,k = map(int,input().rstrip().split())
coins = []
for i in range(n):
    coin = int(input().rstrip())
    if coin <= 10000:
        coins.append(coin)
    else:
        n = n-1
if not coins:
    print(-1)
    exit()
dp = [ [ float('inf') for _ in range(k+1)] for _ in range(n)]


for i in range(n):
    for j in range(1,k+1):
        if coins[i] > j:
            dp[i][j] = dp[i-1][j]
        elif coins[i] == j:
            dp[i][j] = 1
        elif coins[i] < j:
            dp[i][j] = min(dp[i-1][j], dp[i][coins[i]] + dp[i][j-coins[i]])

if dp[n-1][k] == float('inf'):
    print(-1)
    exit()
print(dp[n-1][k])