import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())

visited = dict()
queue = deque()

visited[N] = 0
# x,시간,경로
queue.append((N,0))

cnt = 0
min_time = float('inf')
while queue:
    x,t = queue.popleft()
    # 최소 도달 시간 이상의 시간은 탐색할 필요가 없다.
    if t > min_time:
        break
    # 도착점 도달 시 카운팅 및 최소 시간 등록    
    if x == M:
        cnt += 1
        min_time = t
        continue
    # 방문하지 않으면 방문 체크하고 다음 방문
    for ax, sx in ((1,1),(-1,1), (0,2)):
        xx = sx*x + ax
        if 0 <= xx <= 100000:
            # 이전에 방문하지 않음
            if not xx in visited.keys() :
                visited[xx] = t+1
                queue.append((xx,t+1))
            # 이전에 방문함
            else:
                # 같은 시간에 방문했는데 경로가 다르면 탐색을 이어나감(같은 시간에 같은 지점을 방문했다면 항상 다른 경로, 탐색 중인 모든 경로는 다르다.)
                if visited[xx] == t+1:
                    queue.append((xx,t+1))

print(min_time)
print(cnt)
#
# 현재 위치가 2일 때 +1과 x2는 결과는 같지만 다른 방법이다..!
# 최단 거리인데 경로까지 고려하는 탐색을 해야한다면, 같은 level의 각 노드에서 방문하는 다음 목적지가 같더라도 중복 탐색을 이어나가야 한다. (이른 level이라면 최단 거리가 아니기 때문에 고려할 필요 x) 
# 경로를 고려한다 -> 방문했던 노드도 재방문 해야할 수 있다.
