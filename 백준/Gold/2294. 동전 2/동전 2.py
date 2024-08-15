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
dp = [ float('inf') for _ in range(k+1)]

for i in range(n):
    for j in range(coins[i],k+1):
        if coins[i] == j:
            dp[j] = 1
        elif coins[i] < j:
            dp[j] = min(dp[j], 1 + dp[j-coins[i]])
if dp[k] == float('inf'):
    print(-1)
    exit()
print(dp[k])


# 최적화
# 바로 이전 solution만 이용하기 때문에 1차원으로도 가능
# 사용할 코인부터 저장해도 됨
