from collections import deque
def solution(places):
    '''
    P근처에 BFS로 2칸 안에 또다른 P를 만나면 거리두기를 못 지킨 것
    O만 갈 수 있음, X는 못감
    '''

    def bfs(start):
        q = deque()
        q.append((start[0], start[1], 0))
        visited = set()
        visited.add(start)
        while q:
            y, x, cnt = q.popleft()
            #print(y,x,cnt)
            if place[y][x] == 'P' and cnt != 0:
                return False
            for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
                yy = y + dy
                xx = x + dx
                if 0 <= yy < 5 and 0 <= xx < 5 and cnt < 2:
                    if not (yy,xx) in visited and place[yy][xx] != 'X':
                        q.append((yy, xx, cnt + 1))
        return True
                            
                    
    result = []
    for place in places:
        flag = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs((i,j)): # 실패 시
                        flag = True
                        break
            if flag:
                break
        if flag:
            result.append(0)
        else:
            result.append(1)
    print(result)    
    return result