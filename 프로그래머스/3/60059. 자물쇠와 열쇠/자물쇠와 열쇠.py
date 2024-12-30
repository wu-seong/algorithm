'''
key의 돌기 부분으로 Lock의 홈 부분을 메워야 한다.
key는 움직이거나 회전시킬 수 있다.
브루투 포스?
현재 key로 만들 수 있는 모든 경우 * 모든 블록 확인하기
40*40*4 = 6400 * 400 = 2560000 256만 ㄱㅊ을듯

가로세로를 lock길이의 3배로 늘리기 빈 부분은 0으로
key는 그대로 두고 lock을 옮기면서 겹치는 부분을 and연산한다.
lock 부분이 모두 1이면 True임


'''
    
from copy import deepcopy
from collections import deque
def solution(key, lock):
    M, N = len(key), len(lock)
    
    def rotate(arr):
        for i in range(M):
            for j in range(i,M):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        for i in range(M):
            arr[i].reverse()
            
    def is_unlocked(y, x):
        board = [[0 for _ in range(N + 2*M)] for _ in range(N + 2*M)]
        # lock 표시
        for i in range(N):
            for j in range(N):
                board[i+M][j+M] = lock[i][j]
        
        # key 표시하기
        for i in range(M):
            for j in range(M):
                if key[i][j]:
                    board[i+y][j+x] += 1
        # for b in board:
        #     print(b)
        # print()
        # unlock check하기
        for i in range(N):
            for j in range(N):
                if not board[i+M][j+M] == 1:
                    return False
        return True

    for i in range(N+M+1):
        for j in range(N+M+1):
            if is_unlocked(i,j):
                return True
    for k in range(3):
        rotate(key)
        for i in range(N+M+1):
            for j in range(N+M+1):
                if is_unlocked(i,j):
                    return True
    return False
            