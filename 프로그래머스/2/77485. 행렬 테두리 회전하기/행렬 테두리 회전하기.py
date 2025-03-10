'''
맨 처음에 하나를 저장하고 민 뒤에 땡겨오는 식으로 구현
위부터 반 시계 방향으로
'''
from collections import deque
def solution(rows, columns, queries):
    array = [[ columns*i + j+1 for j in range(columns)] for i in range(rows)]
    #print(array)
    result = []
    def rotate(sy,sx,ey,ex):
        nonlocal array, result
        print(sy,sx,ey,ex)
        temp = array[sy][ex]
        min_value = temp
        # 윗줄 밀기
        for i in range(ex, sx, -1):
            min_value = min(min_value, array[sy][i-1])
            array[sy][i] = array[sy][i-1]
        # 왼쪽줄
        for i in range(sy, ey):
            min_value = min(min_value, array[i+1][sx])
            array[i][sx] = array[i+1][sx]
        # 아랫줄 밀기
        for i in range(sx, ex):
            min_value = min(min_value, array[ey][i+1])
            array[ey][i] = array[ey][i+1]
        # 오른쪽줄
        for i in range(ey, sy, -1):
            min_value = min(min_value, array[i-1][ex])
            array[i][ex] = array[i-1][ex]
        array[sy+1][ex] = temp
        result.append(min_value)
        # for a in array:
        #     print(a)
    for q in queries:
        sy, sx, ey, ex = q
        rotate(sy-1,sx-1,ey-1,ex-1)
    #print(result)
    return result