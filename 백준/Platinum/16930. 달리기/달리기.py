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

    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        for k in range(1,K+1):
            xx = x+(dx*k)
            yy = y+(dy*k)
            if 1 <= xx <= N and 1 <= yy <= M:
                # 벽이면 그 방향으로 탐색 못함
                if gym[xx][yy] == '#':
                    break
                # 빈칸이면 방문 여부 확인
                else:
                    # 이전에 방문 o
                    if visited[xx][yy][0]:
                        # 더 빠른 시간에 방문 했더라면 그 방향으로 더 이상 탐색 x (이미 같거나 더 빠른시간으로 탐색이 진행 됐으므로)
                        if visited[xx][yy][1] < t+1:
                            break
                        # 내가 방문한 시간이 같거나 더 이른 경우, (사실 같을 수는 있어도 더 이를 순 없다.)
                        else:
                            visited[xx][yy][1] = t+1
                    # 이전에 방문 x 방문체크하고 방문한 시간 남기기
                    else:
                        visited[xx][yy][0] = True
                        visited[xx][yy][1] = t+1
                        queue.append((xx,yy,t+1))
            # 체육관 외부
            else:
                break
print("-1")


# 단순 상하좌우 탐색이 아니라 상하좌우 방향으로 K만큼 탐색이기 때문에 몇가지 더 고려해야함
# 1. 현재 방향으로의 탐색이 벽에 막힌적이 있는지
# 2. 현재 방향으로의 탐색이 이미 진행된적이 있는지 (이 경우 탐색하지 않음)
# 3. 현재 방향의 탐색과 수직 방향의 탐색경로가 겹친적이 있는지 이루어진적이 있는지(겹친 칸의 시간이 같다면 겹친 칸의 진행 방향으로의 칸은 t+1을 가지기 때문에 시간이 더 빠르지 않다면 탐색 해주어야 한다.)
