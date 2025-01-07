def solution(T, W, positions):
    # 나무 1과 나무 2에 떨어지는 자두 개수 기록
    tree_1 = [0] * (T + 1)
    tree_2 = [0] * (T + 1)

    for t, pos in enumerate(positions, start=1):
        if pos == 1:
            tree_1[t] = 1
        else:
            tree_2[t] = 1

    # DP 테이블 초기화
    dp = [[0] * (T + 1) for _ in range(W + 1)]

    # DP 상태 전이
    for t in range(1, T + 1):  # 시간 t
        for w in range(W + 1):  # 이동 횟수 w
            if w % 2 == 0:  # 현재 위치가 나무 1
                dp[w][t] = dp[w][t - 1] + tree_1[t] # 위치를 옮기지 않고 1번에 떨어지는 것을 획득(0일 수도 있음)
                if w > 0:
                    dp[w][t] = max(dp[w][t], dp[w - 1][t - 1] + tree_2[t]) # 위치를 옮길 수 있으면 2번으로 위치를 옮겨서 받아먹기, 둘 중 큰 것 채택
            else:  # 현재 위치가 나무 2
                dp[w][t] = dp[w][t - 1] + tree_2[t]
                if w > 0:
                    dp[w][t] = max(dp[w][t], dp[w - 1][t - 1] + tree_1[t])

    # 최대값 계산
    return max(dp[w][T] for w in range(W + 1))

# 입력
T, W = map(int, input().split())
positions = [int(input()) for _ in range(T)]

# 출력
print(solution(T, W, positions))
