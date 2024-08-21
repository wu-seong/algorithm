def solution(money):
    # dp1: 0번을 선택하지 않았을 때, dp2: 선택했을 때
    dp1 = [0 for _ in range(len(money))]
    dp2 = [0 for _ in range(len(money))]
    dp1[1] = money[1]
    for i in range(2,len(money)):
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1])
    
    dp2[0] = money[0]
    dp2[1] = money[0]
    for i in range(2,len(money)-1):
        dp2[i] = max(dp2[i-2] + money[i], dp2[i-1])
    answer = max(dp1[-1],dp2[-2])
    #print(dp1,dp2)
    return answer