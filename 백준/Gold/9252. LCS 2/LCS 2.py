import sys
input = sys.stdin.readline
print = sys.stdout.write
s1 = list(input().rstrip())
s2 = list(input().rstrip())
s1.insert(0,0)
s2.insert(0,0)
M = len(s1)-1
N = len(s2)-1

dp = [ [[0,()] for _ in range(N+1)]for _ in range(M+1)]
# [1]에 이전 문자열 위치를 저장 
max_length = 0
for i in range(1,M+1):
    for j in range(1,N+1):
        if s1[i] == s2[j]:
            dp[i][j][0] = dp[i-1][j-1][0] + 1
            dp[i][j][1] = (i-1,j-1)
        else:
            dp[i][j][0] = max(dp[i][j-1][0], dp[i-1][j][0])
            dp[i][j][1] = (i,j-1) if dp[i][j-1][0] >= dp[i-1][j][0] else (i-1,j)
        max_length = max(dp[i][j][0], max_length)

print("%d\n" %max_length)
if max_length == 0:
    exit()

# 정보를 역추적
n,m = N,M
r_str = []
while n != 0 and m != 0:
    next_n = dp[m][n][1]
    # 새로운 문자가 추가된 경우에만 문자를 추가
    if next_n == (m-1,n-1):
        r_str.append(s2[n])
    m,n = next_n
r_str.reverse()
for c in r_str:
    print("%s" %c)
print("\n")
    