def solution(n):
    # n*n 배열 만들기
    # 0행 -> n-1행 0열 
    # 1열 -> n-1열 n-1행
    # n-2행,열 -> 1행,열
    
    # 2행 -> n-2행 1열
    # 2열 -> n-3열 n-2행
    # n-3행  -> 3행, 행보다 1작은열 
    
    #1 -> 1
    #2 -> 3
    #3 -> 6
    #4 -> 10
    #5 -> 15
    #6 -> 21 
    #n(n+1)/2 
    
    array = [[0 for _ in range(n)] for _ in range(n)]
    i = 1
    start_row = 0
    end_row = n
    start_col = 0
    end_col = n
    row = 0
    col = 0
    d = 0
    while i <= n*(n+1)/2:
        for j in range(start_row, end_row): #내려가면서 
            array[j][col] = i
            i += 1
        for j in range(col+1,end_col): #오른쪽으로 가면서
            array[end_row-1][j] = i
            i += 1
        for j in range(end_row-2, start_row, -1): # 올라가면서
            array[j][j-d] = i
            i += 1
        start_row += 2
        end_row -= 1
        col += 1
        end_col -= 2
        d += 1
    answer = []
    for i, a in enumerate(array):
        answer.extend(a[:i+1])
    return answer
    