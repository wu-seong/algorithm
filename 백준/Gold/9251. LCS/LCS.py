import sys

input = sys.stdin.readline

seq1 = list(input().rstrip())
seq2 = list(input().rstrip())
seq1.insert(0,0)
seq2.insert(0,0)
#print(seq1, seq2)
dp = [ [0 for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]

max_len = 0

for i in range(1,len(seq1)):
    for j in range(1,len(seq2)):
        if seq1[i] == seq2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        max_len = max(max_len, dp[i][j])
print(max_len)

# 먼저 1차원적으로 DP를 생각한다
# 1개의 수열에 대해 어떤 길이가 1인 수열의 포함 여부를 판단한다고 하면
# 해당 수열의 길이가 1 ~ N 일 때를 순차적으로 구한다고 생각하고
# 길이가n 일때의 수열의 포함 여부는 n-1 번째의 까지의 수열의 포함 여부 or 현재 원소의 포함 여부를 보면 된다.

# 경우의 수가 2차원이기 때문에 dp 테이블도 2차원으로 만들어야 한다
# 앞서 예시에서 수열의 고통 부분을 판단하는 것이 길이가 1이 아니라 N 이라면

# 수열의 길이가 0일 때는 서로의 모든 공통 부분 수열의 길이가 0이니 0으로 초기화한다.
# 다음 원소를 추가할 때 
# 추가된 원소가 같은 원소라면 서로 추가하기 전 길이에 + 1

# 다음원소가 한쪽 수열에만 있다면 이 원소를 추가하기 전인  
# 수열 양쪽의 길이를 비교후 더 큰 쪽을 채택