def solution(info, n, m):
    memo = {}  # DP 메모이제이션 딕셔너리

    def dfs(idx, sumA, sumB):
        # B도둑이 흔적 한도를 넘기면 즉시 중단
        if sumB >= m:
            return float('inf')  # 불가능한 경우를 의미
        
        # 모든 물건을 고려했을 때
        if idx == len(info):
            return sumA if sumA < n else float('inf')  # A도둑이 초과하면 불가능
        
        # 메모이제이션 확인
        if (idx, sumA, sumB) in memo:
            return memo[(idx, sumA, sumB)]
        
        # 현재 물건을 A가 훔치는 경우와 B가 훔치는 경우를 탐색
        pick_A = dfs(idx + 1, sumA + info[idx][0], sumB)  # A가 훔치는 경우
        pick_B = dfs(idx + 1, sumA, sumB + info[idx][1])  # B가 훔치는 경우

        # 두 경우 중 최소값 선택
        memo[(idx, sumA, sumB)] = min(pick_A, pick_B)
        return memo[(idx, sumA, sumB)]

    result = dfs(0, 0, 0)
    
    return result if result != float('inf') else -1
