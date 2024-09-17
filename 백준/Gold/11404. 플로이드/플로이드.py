import sys
input = sys.stdin.readline
print = sys.stdout.write
V = int(input().rstrip())
E = int(input().rstrip())

dp = [ [float('inf') for _ in range(V)] for _ in range(V) ]
for _ in range(E):
    u,v,w = map(int, input().rstrip().split())
    if dp[u-1][v-1] > w:
        dp[u-1][v-1] = w
for i in range(V):
    dp[i][i] = 0

for k in range(V):
    for s in range(V):
        for e in range(V):
            dp[s][e] = min(dp[s][e], dp[s][k] + dp[k][e])
for s in range(V):            
    for e in range(V):
        if dp[s][e] == float('inf'):
            print("0 ")
            continue
        print("%d " %dp[s][e])
    print("\n")