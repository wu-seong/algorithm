def solution(alp, cop, problems):
    N = len(problems)
    max_alp = 0
    max_cop = 0
    for i in range(N):
        max_alp = max(max_alp, problems[i][0])
        max_cop = max(max_cop, problems[i][1])
    dp = [ [ 10**6 for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    # 처음부터 다 풀 수 있는 경우
    if alp > max_alp and cop > max_cop:
        return 0
    # 알고력만 높을 때 
    elif alp > max_alp:
        alp = max_alp
    # 코딩력만 높을 때
    elif cop > max_cop:
        cop = max_cop
    
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            # 공부하는 걸로 갱신
            if i+1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)        
            if j+1 <= max_cop:           
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            # 풀 수 있는 문제 가져오기
            for p in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = p
                if alp_req <= i and cop_req <= j:
                    # 알고력, 코딩력이 목표치를 넘어갈 때
                    if i+alp_rwd > max_alp and j+cop_rwd > max_cop:
                        dp[max_alp][max_cop] = min(dp[max_alp][max_cop] ,dp[i][j]+cost)
                    # 알고력만 목표치를 넘어갈 때
                    elif i+alp_rwd > max_alp: 
                        dp[max_alp][j+cop_rwd] = min(dp[max_alp][j+cop_rwd] ,dp[i][j]+cost)
                    # 코딩력만 목표치를 넘어갈 때
                    elif j+cop_rwd > max_cop: 
                        dp[i+alp_rwd][max_cop] = min(dp[i+alp_rwd][max_cop] ,dp[i][j]+cost)
                    # 아무것도 목표치를 넘지 않을 때
                    else:
                        dp[i+alp_rwd][j+cop_rwd] = min(dp[i+alp_rwd][j+cop_rwd] ,dp[i][j]+cost)

    answer = dp[max_alp][max_cop]
    return answer