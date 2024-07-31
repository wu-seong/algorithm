import sys
from collections import deque

input = sys.stdin.readline

dm = (1,-1,0,0)
dn = (0,0,1,-1)
M,N = map(int, input().rstrip().split())

tomato = [ [0 for _ in range(M)] for _ in range(N)]
# 방문 여부
visited = [ [False for _ in range(M)] for _ in range(N)] 
for n in range(N):
    tomato[n] = list(map(int, input().rstrip().split()))


queue = deque()

# 익은 토마토 모두 방문하고 queue에 넣기
for n in range(N):
    for m in range(M):
        if tomato[n][m] == 1:
            visited[n][m] = True
            queue.append((n,m,0))


max = 0
# 여러 누트노드에서 한 level씩 탐색 시작
# 가장 높은 level을 max에 저장
while queue:
    n,m,d = queue.popleft()
    if max < d:
        max = d
    #print(n,m,d)
    # 익은 토마토 전파
    for i in range(4):
        # 가장자리 체크
        next_n = n+dn[i]
        next_m = m+dm[i]
        if ((0 <= next_n < N) and (0<= next_m < M)):
            # 안익은 토마토에 전파
            if  tomato[next_n][next_m] == 0 and not visited[next_n][next_m]:
                visited[next_n][next_m] = True
                queue.append( (next_n, next_m, d+1) )

for n in range(N):
    for m in range(M):
        if tomato[n][m] == 0 and not visited[n][m]:
            print("-1")
            exit()
print(max)


# 시작점이 여러개일 수도 있다..!!, 루트노드가 명확하게 여러개가 주어진다면 동시 탐색을 할 것