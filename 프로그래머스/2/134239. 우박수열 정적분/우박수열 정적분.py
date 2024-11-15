def solution(k, ranges):
    '''
    콜라츠 추측으로 1 구하고 과정 저장하기 + 해당 범위 정적분 저장
    range에 따라서 범위에 따라서
    
    정적분 결과 합산
    '''
    
    i = k
    colatz = [i]
    while i != 1:
        if i % 2 == 0:
            i /= 2
        else:
            i = i*3 + 1
        colatz.append(i)
    integral = []
    for i in range(1,len(colatz)):
        bigger, smaller = max(colatz[i], colatz[i-1]), min(colatz[i], colatz[i-1])
        i_result = smaller + (bigger - smaller)*(0.5)
        integral.append(i_result)
    # print(colatz)
    # print(integral)
    result = []
    n = len(colatz) - 1
    #print(n)
    for r in ranges:
        a,b = r
        b = abs(b)
        if n - b < a:
            result.append(-1)
            continue
        #print(r,a,n-b,integral[a:n-b], sum(integral[a:n-b]))
        result.append(sum(integral[a:n-b]))
    #print(result)
    return result
    