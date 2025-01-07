'''
고정석이 없다면?

1개가 있으면
고정 1
2개가 있으면
고정, 교체하기 2
3개가 있으면
dp[i-1] + dp[i-2]
1 2 3
2 1 3
1 3 2

123 12 12
3 * 4 = 12
고정석이면 초기화 및 이전 기록 저장

마지막이면 이전 기록 저장

저장한 것들 모두 곱하기
'''

def solution(N, M):
    dp = [0] * (N+1)
    if N == 1: # 좌석 1개인 경우
        print(1)
        exit()
    # dp초기화
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    i = 3 
    while i <= N:
        dp[i] = dp[i-1] + dp[i-2]
        i += 1
    #print(dp)
    
    # 지정석 저장
    fix = []
    for i in range(M):
        fix.append(int(input()))
    #print(fix)

    if M == 0:
        print(dp[N])
    elif M == 1:
        seat = fix[0]
        print(dp[seat-1] * dp[N-seat])
    else:
        start, end = fix[0], fix[-1]
        length = []
        length.append(start-1)
        length.append(N-end)
        for r in [ fix[i] - fix[i-1] for i in range(1, M)]:
            length.append(r-1)
        result = 1
        #print("legnth", length)
        for l in length:
            result *= dp[l]
        print(result)
        
solution(int(input()), int(input()))
