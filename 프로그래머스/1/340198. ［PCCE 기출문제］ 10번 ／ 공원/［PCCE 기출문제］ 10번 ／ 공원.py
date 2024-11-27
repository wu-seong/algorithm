def solution(mats, park):
    '''
    현재 위치가 -1이면 왼쪽, 위, 대각 중에서 가장 숫자가 작은 것 + 1
    
    왼쪽 위부터 순회하면서 
    현재가 -1이면
    왼쪽, 위, 대각 확인 (범위도 체크)
    현재 위치에서 만들 수 있는 정사각형 갱신하고 최댓값 비교
    '''
    
    n,m = len(park), len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                park[i][j] = 1
            else:
                park[i][j] = 0
    print(park)
    max_result = park[0][0]
    for i in range(1,n):
        for j in range(1,m):
            if park[i][j]: # 깔 수 있는 자리이면
                max_result = max(max_result, 1)
                min_size = min(park[i-1][j], park[i][j-1], park[i-1][j-1])
                park[i][j] = min_size + 1
                max_result = max(max_result, park[i][j])
    for p in park:
        print(p)
    mats.sort()
    print(max_result)
    for i, mat in enumerate(mats):
        if mat > max_result:
            mats = mats[:i]
            break
    if mats:
        print(mats)
        return mats[-1]
    return -1
    
        
        
                    
                        
                
                
        