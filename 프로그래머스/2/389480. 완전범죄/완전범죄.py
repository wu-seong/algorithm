# def solution(info, n, m):
#     length = len(info)
#     dp = [[float('inf') for _ in range(m)] for _ in range(length)]
#     # A를 선택
#     a,b = info[0]
#     dp[0][0] = a
#     # B를 선택
#     if b < m:
#         dp[0][b] = 0
#     print('초기화:', dp)
    
#     for i in range(1, len(info)):
#         a,b = info[i]
#         print(a,b)
#         if m == 1:
#             dp[i][0] = dp[i-1][0] + a
#         for j in range(m-1, -1, -1):
#             # A 선택하는 경우
#             dp[i][j] = dp[i-1][j] + a
#             # B 선택하는 경우 (j+b<m)
#             if j + b < m:
#                 dp[i][j + b] = min(dp[i][j + b], dp[i-1][j])
#     for i in range(len(info)):
#         print(dp[i])
            
def solution(info, n, m):
    length = len(info)
    dp = [[float('inf')] * m for _ in range(length)]

    # 첫 번째 물건 처리
    a, b = info[0]
    dp[0][0] = a  # A가 선택한 경우
    if b < m:
        dp[0][b] = 0  # B가 선택한 경우

    # DP 테이블 채우기
    for i in range(1, length):
        a, b = info[i]
        
        for j in range(m-1, -1, -1):  # 역순 탐색 (값이 덮어써지는 문제 방지)
            # A를 선택하는 경우
            dp[i][j] = min(dp[i][j], dp[i-1][j] + a)

            # B를 선택하는 경우 (j+b가 m을 넘지 않는다면)
            if j + b < m:
                dp[i][j + b] = min(dp[i][j + b], dp[i-1][j])

    # 결과 찾기
    min_value = float('inf')
    for value in dp[length - 1]:
        if value < n:
            min_value = min(min_value, value)

    return min_value if min_value != float('inf') else -1
