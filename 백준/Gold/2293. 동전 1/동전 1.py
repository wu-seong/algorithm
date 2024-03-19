import sys
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().rstrip().split())


coin = []
for i in range(n):
    value = int(input().rstrip())
    coin.append(value)
#print("%s\n"%coin)

dp = [ [0 for _ in range(k+1)] for _ in range(2)]
for v in dp[0]:
    # 1원 동전으로 k원을 만드는 경우의 수 -> 모두 1
    v = 1
#print("%s\n"%dp[0])
for c in coin:
    for j in range(k+1):
        if j < c:
            dp[1][j] = dp[0][j]
        elif j == c:
            dp[1][j] = dp[0][j] + 1
        else:
            dp[1][j] = dp[0][j] + dp[1][j-c]

    dp[0] = dp[1]
    
print("%d\n"%dp[1][k])