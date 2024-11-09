def solution(wallpaper):
    '''
    '#' 인 것 중 가장 위쪽 ,가장 왼쪽, 가장 오른, 가장 아래를 골라서
    위 - 아래, 오른 - 왼 절댓값 구해서 더하기
    1,0  왼쪽 위는 좌표 그대로 오른쪽 아래는 1씩 더해서 계산하기
    '''
    
    '''
    #이 있는 좌표를 구하기
    그 중 y의 최대 최소, x의 최대 최소 구하기
    '''
    coordinates = []
    row_n = len(wallpaper)
    col_n = len(wallpaper[0])
    for i in range(row_n):
        for j in range(col_n):
            if wallpaper[i][j] == '#':
                coordinates.append((i,j))
    #print(coordinates)
    max_y = max(coordinates, key=lambda x: x[0])[0]
    max_x = max(coordinates, key=lambda x: x[1])[1]
    min_y = min(coordinates, key=lambda x: x[0])[0]
    min_x = min(coordinates, key=lambda x: x[1])[1]
    return [min_y, min_x, max_y+1, max_x+1]
    
    