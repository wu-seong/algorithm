def solution(n, left, right):
    # n번째까지는 n 이후로 n+1
    # left가 ~ n의 몫 + 나머지 몫 + 1보다 작으면 몫 + 1 아니면 나머지 + 1
    # 몇행 몇번째 열인지를 알아내서 그 부분만 구하기
    l_row, r_row = left // n, right//n
    l_col, r_col = left % n, right % n
    result = []
    for i in range(l_row, r_row + 1):
        for j in range(n):
            if i == l_row and j < l_col: # 시작
                continue
            result.append(max(i+1, j+1))
            if i == r_row and j == r_col: # 끝
                #print(result)
                return result