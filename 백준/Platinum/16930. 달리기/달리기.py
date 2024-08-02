# 3 4 4
# ....
# ###.
# ....
# 1 1 3 1

import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int, input().rstrip().split())


gym = [list(input().rstrip()) for _ in range(N)]
gym.insert(0,0)
for i in range(1,N+1):
    gym[i].insert(0,0)
#print(gym)
visited = [ [[False,0] for _ in range(M+1)] for _ in range(N+1)]
start_x, start_y, end_x, end_y = map(int ,input().rstrip().split())


# 시작점에서 탐색 시작
visited[start_x][start_y][0] = True
visited[start_x][start_y][1] = 0

# bfs
queue = deque()
queue.append((start_x,start_y,0))
while queue:
    x,y,t = queue.popleft()
    if (x,y) == (end_x,end_y):
        print(t)
        exit()
    # 오른 방향
    for k in range(1,K+1):
        if 1 <= x <= N and 1 <= y+k <= M:
            if gym[x][y+k] == '#':
                #print("오른쪽으로는 못 감")
                break
            if visited[x][y+k][0]:
                if visited[x][y+k][1] < t+1:
                    break
                else:
                    visited[x][y+k][1] = t+1
            if not visited[x][y+k][0] and gym[x][y+k] == '.':
                visited[x][y+k][0] = True
                visited[x][y+k][1] = t+1
                queue.append((x,y+k,t+1))
        else:
            #print("맵 밖이라 오른쪽으로는 못 감")
            break
    # 왼 뱡향
    for k in range(1,K+1):
        if 1 <= x <= N and 1 <= y-k <= M:
            if gym[x][y-k] == '#':
                #print("왼쪽으로는 못 감")
                break
            if visited[x][y-k][0]:
                if visited[x][y-k][1] < t+1:
                    break
                else:
                    visited[x][y-k][1] = t+1
            if not visited[x][y-k][0] and gym[x][y-k] == '.':
                visited[x][y-k][0] = True
                visited[x][y-k][1] = t+1
                queue.append((x,y-k,t+1))
        else:
            #print("맵 밖이라 왼쪽으로는 못 감")
            break
    # 윗 방향
    for k in range(1,K+1):
        if 1 <= x+k <= N and 1 <= y <= M:
            if gym[x+k][y] == '#':
                #print("윗방향으로는 못 감")
                break
            if visited[x+k][y][0]:
                if visited[x+k][y][1] < t+1:
                    break
                else:
                    visited[x+k][y][1] = t+1
            if not visited[x+k][y][0] and gym[x+k][y] == '.':
                visited[x+k][y][0] = True
                visited[x+k][y][1] = t+1
                queue.append((x+k,y,t+1))
        else:
            #print("맵 밖이라 위쪽으로는 못 감")
            break
    # 아랫 방향
    for k in range(1,K+1):
        if 1 <= x-k <= N and 1 <= y <= M:
            if gym[x-k][y] == '#':
                #print("아랫방향으로는 못 감")
                break
            if visited[x-k][y][0]:
                if visited[x-k][y][1] < t+1:
                    break
                else:
                    visited[x-k][y][1] = t+1
            if not visited[x-k][y][0] and gym[x-k][y] == '.':
                visited[x-k][y][0] = True
                visited[x-k][y][1] = t+1
                queue.append((x-k,y,t+1))
        else:
            #print("맵 밖이라 아랫쪽으로는 못 감")
            break
print("-1")

# 탐색을 하다 visited를 만나면 그 즉시, 

# 끝점 도달 시 지난 시간 출력