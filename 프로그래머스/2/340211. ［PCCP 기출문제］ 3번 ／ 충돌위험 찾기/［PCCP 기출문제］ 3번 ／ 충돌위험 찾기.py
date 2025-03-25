'''
여러 지점에서 동시에 bfs를 해서
현재 지점에 다른 로봇이 있는지를 판단해서 카운팅하기
'''

from collections import deque
def solution(points, routes):
    
    p_n = len(points)
    n = len(routes)
    # n번째 로봇들의 시작 위치 = routes의 시작점을 인덱스로 하는 포인트
    points = [ [points[i][j]-1 for j in range(2)] for i in range(p_n)]
    routes = [ [routes[i][j]-1 for j in range(len(routes[i]))] for i in range(n)]
    #print(points)
    
    location = [0] * n # 0번째 로봇의 위치 (y,x)
    step = [1] * n
    finish = [False] * n
    for i, l in enumerate(routes):
        s = l[0]
        location[i] = points[s]
    print('시작위치', location)
    
    #로봇의 현재 위치 중 겹치는 것이 있는지 (로봇들이 모두 움직인 후에 한번 확인)
    
    def count_in_many():
        du = set()
        
        # 아직 활동 중인 로봇들을 대상으로 겹치는 것 확인
        for i in range(n):
            if finish[i]:
                continue
            for j in range(i+1,n):
                # 아직 step이 진행중인 것에 한정해서만 카운팅
                if not finish[j]:                 
                    #print(location[i], location[j])
                    if location[i] == location[j]:
                        y,x = location[i]
                        du.add((y,x))
        #print('겹치는 횟수 확인하기', len(du))
        return len(du)
    
    # 다음 좌표를 구하는 함수
    def get_next(y,x,ey,ex):
        if y < ey:
            return (y+1, x)
        elif y > ey:
            return (y-1, x)
        else:
            if x < ex:
                return (y, x+1)
            elif x > ex:
                return (y, x-1)
            
    
    q = deque()
    tq = deque()
    for i, l in enumerate(location):
        y,x = l
        q.append((i,y,x,0))
    
    result = 0
    print(q)
    while q:
        i,y,x,l = q.popleft()
        location[i] = [y,x]
        # 마지막 로봇 이동
        if q and q[0][3] == l + 1 or not q:
            # 카운팅
            result += count_in_many()
            # 근데 목적지에 도착한 것이 있으면 다음 목적지 갱신
            for j in range(n):
                dst_y, dst_x = points[routes[j][step[j]]]
                #print(location[j], [dst_y, dst_x] )
                if location[j] == [dst_y, dst_x]:
                    if step[j] + 1 >= len(routes[j]):
                        #print(j,'번 끝남')
                        finish[j] = True
                    else:
                        step[j] += 1    
                        dst_y, dst_x = points[routes[j][step[j]]]
                if not finish[j]:
                    ny, nx = get_next(location[j][0], location[j][1] ,dst_y,dst_x)
                    q.append((j,ny,nx,l+1))
        #print(q)

    print(result)
    
    return result