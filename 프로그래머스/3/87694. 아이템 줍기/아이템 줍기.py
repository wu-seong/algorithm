'''
출발점에서 끝점까지의 거리를 구하기

일단 모든 사각형에 대해서 경로를 이어놓고 갈림길이 나올 시에 어디로 갈지만 판단을 잘하면 됨

갈림길이 나오면 무조건 꺾어야 함
꺾어서 간 점이 이전에 돌던 사각형의 내부이면 안됨

그렇게 bfs해서 구하기


갈림길을 통해 간 해당 점이 어떤 사각형의 두 꼭짓점 사이에 있는 점인지를 판단하는 함수 

2차원 map에 갈 수 있는 길을 1로 표시하기

다음 갈 곳 중에서 진행방향과 같은데 다른 사각형이면 못감

'''
from collections import deque
def is_in(t_y, t_x, r):
    s_x, s_y, e_x, e_y = r
    #print()
    if s_y < t_y < e_y and s_x < t_x < e_x:
        #print('내부임', t_y,t_x, r)
        return True
    #print('내부 아님', t_y,t_x, r)
    return False

def make_map(rectangle, cmap, sx, sy, ex, ey, i):
    for y in range(sy, ey):
        for osx, osy, oex, oey in rectangle:
            if osy < y+1 < oey and osx < sx < oex:
                break
        else:
            cmap[y][sx].append((y+1,sx,i))
            cmap[y+1][sx].append((y,sx,i))
        
        for osx, osy, oex, oey in rectangle:
            if osy < y+1 < oey and osx < ex < oex:
                break
        else:
            cmap[y][ex].append((y+1,ex,i))
            cmap[y+1][ex].append((y,ex,i))
        
    for x in range(sx, ex):
        for osx, osy, oex, oey in rectangle:
            if osy < sy < oey and osx < x+1 < oex:
                break
        else:
            cmap[sy][x].append((sy,x+1,i))
            cmap[sy][x+1].append((sy,x,i))
        
        for osx, osy, oex, oey in rectangle:
            if osy < ey < oey and osx < x+1 < oex:
                break
        else:
            cmap[ey][x].append((ey,x+1,i))
            cmap[ey][x+1].append((ey,x,i))

def bfs(cmap, sy, sx, ty, tx, rectangle):
    visited = set()
    q = deque()
    visited.add((sy,sx))
    q.append((sy,sx,0))
    print(ty, tx)
    while q:
        y,x,l = q.popleft()
        # print(y,x,l,r)
        # print('next:',cmap[y][x])
        if y == ty and x == tx:
            return l
        for yy,xx,i in cmap[y][x]: 
            # 방문했던 곳 가지 않음
            if (yy,xx) in visited:
                continue
            # 다음 방문
            visited.add((yy,xx))
            q.append((yy,xx,l+1))
    print(visited)
    
def scale_up(rectangle):
    for i, r in enumerate(rectangle):
        for j in range(4):
            rectangle[i][j] = r[j]*2
    #print(rectangle)
    return rectangle
def solution(rectangle, characterX, characterY, itemX, itemY):
    scale_up(rectangle)
    cmap = [[[] for _ in range(102)] for _ in range(102)]
    
    for i, v in enumerate(rectangle):
        sx, sy, ex, ey = v
        make_map(rectangle, cmap, sx, sy, ex, ey, i)
    
    for m in cmap[:12]:
        print(m[:12])
    result = bfs(cmap, characterY*2, characterX*2, itemY*2, itemX*2, rectangle)
    print(result)
    return result//2
    
        
    