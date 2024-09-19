import sys
input = sys.stdin.readline
print = sys.stdout.write

V,E = map(int, input().rstrip().split())

dp = [[ float('inf') for _ in range(V)] for _ in range(V)]
for _ in range(E):
    u,v = map(int, input().rstrip().split())
    dp[u-1][v-1] = 1
for i in range(V):
    dp[i][i] = 0
for k in range(V):
    for s in range(V):
        for e in range(V):
            dp[s][e] = min(dp[s][e], dp[s][k] +dp[k][e])
n = int(input().rstrip())
for _ in range(n):
    u,v = map(int ,input().rstrip().split())
    if dp[u-1][v-1] != float('inf'):
        print("-1\n")
    elif dp[v-1][u-1] != float('inf'):
        print("1\n")
    else:
        print("0\n")
