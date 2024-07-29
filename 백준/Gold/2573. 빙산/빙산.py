# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0

import sys
from  collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

ice = [list(map(int, input().rstrip().split())) for _ in range(N)]

ice_dict = {}
for i in range(N):
    for j in range(M):
        if ice[i][j] > 0:
            ice_dict[(i,j)] = ice[i][j]

def count_around_sea(i,j):
    cnt = 0
    if ice[i-1][j] == 0:
        cnt += 1
    if ice[i][j+1] == 0:
        cnt += 1
    if ice[i][j-1] == 0:
        cnt += 1
    if ice[i+1][j] == 0:
        cnt += 1
    return cnt
def search_next_ice(i,j):
    if ice[i-1][j] > 0 and not visited[i-1][j]:
        return (i-1,j)
    if ice[i][j+1] > 0 and not visited[i][j+1]:
        return (i,j+1)
    if ice[i][j-1] > 0 and not visited[i][j-1]:
        return (i,j-1)
    if ice[i+1][j] > 0 and not visited[i+1][j]:
        return (i+1,j)
    return False

# 빙산이 다 녹을 때 까지 BFS를 반복

cnt = 0
all_melt = False
while not all_melt:
    melt_count = {}
    first_find = True
    visited = [ [False for _ in range(M)] for _ in range(N)]
    queue = deque()

    # 빙산을 탐색하기
    for key in ice_dict:
        i,j = key
        if ice[i][j] > 0 and first_find:
            first_find = False
            visited[i][j] = True
            queue.append((i,j))
            while queue:
                r,c = queue.popleft()
                melt_count[(r,c)] = count_around_sea(r,c)
                if ice[r][c+1] > 0 and not visited[r][c+1]:
                    visited[r][c+1] = True
                    queue.append((r,c+1))
                if ice[r][c-1] > 0 and not visited[r][c-1]:
                    visited[r][c-1] = True
                    queue.append((r,c-1))
                if ice[r+1][c] > 0 and not visited[r+1][c]:
                    visited[r+1][c] = True
                    queue.append((r+1,c))
                if ice[r-1][c] > 0 and not visited[r-1][c]:
                    visited[r-1][c] = True
                    queue.append((r-1,c))
        # 이후에 방문하지 않은 다른 빙산을 찾으면 2개 이상으로 갈라진 것            
        elif ice[i][j] > 0 and not visited[i][j] and not first_find:
            # for i in range(N):
            #     print(visited[i])
            # for i in range(N):
            #     print(ice[i])
            print(cnt)
            exit()
    all_melt = True
    cnt += 1
    for key in melt_count.keys():
        r,c = key
        if ice[r][c] - melt_count.get(key) < 0:
            ice[r][c] = 0
        else:
            all_melt = False
            ice[r][c] -= melt_count.get(key)

print("0")

