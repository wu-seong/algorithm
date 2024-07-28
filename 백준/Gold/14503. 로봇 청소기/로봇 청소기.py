import sys
from collections import deque
input = sys.stdin.readline

move_east = (0,1)
move_north = (-1,0)
move_west = (0,-1)
move_south = (1,0)
back = [ (1,0), (0,-1), (-1,0), (0,1)]

def get_not_exist_clean(r,c,d):
    #북
    if(d == 0):
        if room[r][c-1] == 0:
            return (r,c-1,3)
        elif room[r+1][c] == 0:
            return (r+1,c,2)
        elif room[r][c+1] == 0:
            return (r,c+1,1)
        elif room[r-1][c] == 0:
            return (r-1,c,0)
    #동
    if(d == 1):
        if room[r-1][c] == 0:
            return (r-1,c,0)
        elif room[r][c-1] == 0:
            return (r,c-1,3)
        elif room[r+1][c] == 0:
            return (r+1,c,2)
        elif room[r][c+1] == 0:
            return (r,c+1,1)
    #남
    if(d == 2):
        if room[r][c+1] == 0:
            return (r,c+1,1)
        elif room[r-1][c] == 0:
            return (r-1,c,0)
        elif room[r][c-1] == 0:
            return (r,c-1,3)
        elif room[r+1][c] == 0:
            return (r+1,c,2)
    #서
    if(d == 3):
        if room[r+1][c] == 0:
            return (r+1,c,2)
        elif room[r][c+1] == 0:
            return (r,c+1,1)
        elif room[r-1][c] == 0:
            return (r-1,c,0)
        elif room[r][c-1] == 0:
            return (r,c-1,3)
    # 동서남북에 모두 not clean한 칸이 없을 때
    return False


N,M = map(int, input().rstrip().split())
r,c,d = map(int, input().rstrip().split())

room = [ [] for _ in range(N)]

for i in range(N):
    room[i] = list(map(int, input().rstrip().split()))


cnt = 0
queue = deque()
queue.append((r,c,d))
if room[r][c] == 0:
    room[r][c] = 2
    cnt += 1
while queue:
    r,c,d = queue.popleft()
    #print(r,c,d)
    # 청소할 곳이 없다면
    ret = get_not_exist_clean(r,c,d)
    # for i in range(N):
    #     print(room[i])
    if  ret == False:
        d_back = back[d]
        # 뒤가 벽이면 그만 탐색
        if room[r+d_back[0]][c+d_back[1]] == 1:
            print(cnt)
            exit()
        # 뒤가 벽이 아니면 후진
        else:
            if room[r+d_back[0]][c+d_back[1]] == 0:
                room[r+d_back[0]][c+d_back[1]] = 2
                cnt += 1
            queue.append( (r+d_back[0], c+d_back[1], d) )
    # 청소할 곳을 찾으면
    else:
        r,c,d = ret # 청소할 칸과 현재 방향
        room[r][c] = 2
        cnt += 1
        queue.append((r,c,d))

    

