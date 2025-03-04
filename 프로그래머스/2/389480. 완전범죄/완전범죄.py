def solution(info, n, m):
    length = len(info)
    dp = [[float('inf') for _ in range(m)] for _ in range(length)]
    # A를 선택
    a,b = info[0]
    dp[0][0] = a
    # B를 선택
    if b < m:
        dp[0][b] = 0
    print('초기화:', dp)
    
    for i in range(1, len(info)):
        a,b = info[i]
        print(a,b)
        for j in range(m-1, -1, -1):
            # A 선택하는 경우
            dp[i][j] = dp[i-1][j] + a
            # B 선택하는 경우 (j+b<m)
            if j + b < m:
                dp[i][j + b] = min(dp[i][j + b], dp[i-1][j])
    for i in range(len(info)):
        print(dp[i])
        
    result = min(dp[length-1])
    print(result)
    if result < n: 
        return result
    return -1
   