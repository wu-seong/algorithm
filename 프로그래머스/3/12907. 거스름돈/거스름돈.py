'''
거슬러줄 방법의 경우의 수

5원을 거슬러 주는 경우의 수
동전의 종류
  1 2 5
  1 0
  1 1+1
  1 1
  1 
  1
  현재 종류의 동전을 사용하고 합계에서 현재 동전의 가치를 뺀 이전까지의 경우의 수
n원을 거슬러주는 경우의 수 = n
처음 행은 그냥 각 배수마다 1씩

새로운 동전을 사용하는 것과 사용하지 않는 것 중 더 나은 것을 선택?
'''
def solution(n, coin):
    coin.sort()
    m = len(coin)
    dp = [[0 for _ in range(n+1)] for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(1,n+1):
        if j % coin[0] == 0:
            dp[0][j] = 1
    for i in range(1,m):
        c = coin[i]
        for j in range(1,n+1):
            #print(c,j)
            if j < c: # 동전의 종류가 추가되기 전과 같다.
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-c]
    #print(dp)
    return dp[m-1][n]