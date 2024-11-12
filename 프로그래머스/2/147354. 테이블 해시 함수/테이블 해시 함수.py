def solution(data, col, row_begin, row_end):
    '''
    튜플을 정렬한다
    
    범위내의 모든 i에 대해서 S_I를 구한다
    -> 범위내 행만 추출
    -> 해당 행의 각 값을 i로 나눈 나머지의 합 구하기
    
    계속해서 XOR연산을 한다.
    '''
    si_list = []
    data.sort(key = lambda x: (x[col-1], -x[0]))
    data = data[row_begin-1:row_end]
    #print(data)
    for i, row in enumerate(data):
        order = row_begin + i
        r_sum = 0
        for value in row:
            r_sum += value % order
        si_list.append(r_sum)
    #print(si_list)
    
    result = si_list[0]
    for i in range(1,len(si_list)):
        result = result ^ si_list[i]
    #print(result)
    return result