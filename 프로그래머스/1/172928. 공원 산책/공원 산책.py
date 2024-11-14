from collections import deque
def solution(park, routes):
    '''
    Park에서 start지점 찾기
    routes를 순회하면서 각 route에 지정된대로 이동 (s지점부터 시작해서)
    방향으로 반복해서 가는데 장애물이나 맵에서 벗어나면 continue
    '''
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start = (i,j)
    
    n = len(park)
    m = len(park[0])
    direction = {'E': (0,1), 'W': (0,-1), 'N': (-1,0), 'S': (1,0) }
    y, x = start
    for route in routes:
        d, t = route.split(' ')
        t = int(t)
        dy, dx = direction[d]
        #print(d,t,y,x)
        yy = y
        xx = x
        while t > 0:
            yy += dy
            xx += dx
            if 0 <= yy < n and 0 <= xx < m and park[yy][xx] != 'X':
                t -= 1
                continue
            break
        if t == 0: # 끝까지 가능하면 이동
            y = yy
            x = xx
    print(y,x)
    return [y,x]