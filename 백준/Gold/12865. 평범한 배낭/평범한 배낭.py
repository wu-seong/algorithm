import sys
input = sys.stdin.readline

N,K = map(int, input().rstrip().split())
T = [ list(map(int, input().rstrip().split())) for _ in range(N) ]

dp = [ [0 for _ in range(K+1)] for _ in range(N)]

for i in range(1,K+1):
    if i >= T[0][0]:
        dp[0][i] = T[0][1]
        
for i in range(1,N):
    w,v = T[i]
    # 이전 부분해 가져오기 
    for j in range(1,K+1):
        # 새로 추가된 물건을 선택할 수 없을 때는 이전과 같음
        if j < w:
            dp[i][j] = dp[i-1][j]
        # 새로 추가한 물건을 선택하고 나머지 무게를 이전 최댓값으로 채운 것이 더 크다면 최대값 갱신
        else:
            dp[i][j] = max(dp[i-1][j], v+dp[i-1][j-w])
print(dp[N-1][K])
        