import sys
input = sys.stdin.readline
print = sys.stdout.write
s1 = list(input().rstrip())
s2 = list(input().rstrip())
s1.insert(0,0)
s2.insert(0,0)
M = len(s1)-1
N = len(s2)-1

dp = [ [0 for _ in range(N+1)]for _ in range(M+1)]
# [1]에 이전 문자열 위치를 저장 
max_length = 0
for i in range(1,M+1):
    for j in range(1,N+1):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        max_length = max(dp[i][j], max_length)

print("%d\n" %max_length)
if max_length == 0:
    exit()

# 정보를 역추적
n,m = N,M
r_str = ""
while n != 0 and m != 0:
    # 문자가 추가된 경우만 문자열에 추가 
    if dp[m][n] > dp[m-1][n] and dp[m][n] > dp[m][n-1]:
        r_str = s2[n] + r_str
        n = n-1
        m = m-1
        continue
    # 이전과 같은 경우는 이전으로 되추적 
    if dp[m-1][n] > dp[m][n-1]:
        m = m-1
    else:
        n = n-1
print("%s\n" %r_str)
    