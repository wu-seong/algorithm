def solution(r1, r2):
    '''
    각 x에 해당하는 y좌표를 구하기 (1 <= x <= r2)
    큰 원의 y좌표에서 x의 y좌표를 뺀다. (소숫점은 둘 다 버림)  
    + 1 한 것이 한 사분면의 각 점의 정수 좌표 개수
    *4를 하면된다.
    '''
    
    def get_y(x, r):
        return abs((r**2 - x**2)**0.5)
    cnt = 0
    for x in range(r2):
        if x < r1:
            y1 = get_y(x, r1)
        else:
            y1 = 0
        y2 = get_y(x, r2)
        #print(y1,y2)
        if y1 == 0:
            cnt -= 1
        if y1 == int(y1):
            cnt += 1
        cnt += (y2//1) - (y1//1)
    cnt *= 4
    print(cnt)
    return cnt