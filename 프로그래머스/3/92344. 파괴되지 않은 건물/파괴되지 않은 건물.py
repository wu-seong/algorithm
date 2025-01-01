'''
있는 것을 곧이곧대로 더하면 시간초과
시작 행에서 시작 위치와 끝 위치에 N, -N 
마지막 행에서 시작 위치와 끝 위치에 -N, N을 각각 더하기
그다음 각 열, 행 순서로 누적합구하기


그 후에 전체 탐색하며 원래 health를 더한 값이 0을 초과하는 것의 개수를 카운팅
'''
def solution(board, skill):
    N, M = len(board), len(board[0])
    diff = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for t, r1, c1, r2, c2, degree in skill:
        if t == 2:
            degree *= -1
            
        diff[r1][c1] -= degree
        diff[r1][c2+1] += degree
        diff[r2+1][c1] += degree
        diff[r2+1][c2+1] -= degree
        
    for i in range(N+1):
        for j in range(1, M+1):
            diff[i][j] += diff[i][j-1]
    
    for i in range(1, N+1):
        for j in range(M+1):
            diff[i][j] += diff[i-1][j]
    
        
    cnt = 0
    for i in range(N):
        for j in range(M):
            diff[i][j] += board[i][j]
            if diff[i][j] >= 1:
                cnt += 1
    # for d in diff:
    #     print(d)
    return cnt
    
    