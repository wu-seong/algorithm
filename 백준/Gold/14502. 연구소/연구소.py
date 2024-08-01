import sys

input = sys.stdin.readline

dx = (0,0,1,-1)
dy = (1,-1,0,0)

def spread(lab,node):
    y,x = node
    #print(y,x)
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if 0 <= next_y < N and 0 <= next_x < M:
            # 빈칸이고 바이러스가 방문하지 않았다면 퍼뜨림
            if lab[next_y][next_x] == 0:
                lab[next_y][next_x] = 2
                spread(lab, (next_y, next_x))

N,M = map(int, input().rstrip().split())

lab = [ [] for _ in range(N) ]

for i in range(N):
    lab[i] = list(map(int, input().rstrip().split()))


# 랜덤하게 벽을 세운다
# 세울 수 있는 칸을 구해온다.
# 바이러스 칸도 구한다.
virus_location = []
build_possible = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            build_possible.append((i,j))
        elif lab[i][j] == 2:
            virus_location.append((i,j))

max_safe_area = 0

n = len(build_possible)
for x in range(n):
    for y in range(x+1,n):
        for z in range(y+1,n):
            # 서로 다른 3개를 뽑아 벽을 세운다
            w1_y, w1_x = build_possible[x]
            w2_y, w2_x = build_possible[y]
            w3_y, w3_x = build_possible[z]
            lab[w1_y][w1_x] = 1
            lab[w2_y][w2_x] = 1
            lab[w3_y][w3_x] = 1
    
            # 각 바이러스 전파
            for v in virus_location:
                spread(lab,v)
            # 안전영역 구하기
            visited = [ [False for _ in range(M)] for _ in range(N) ]
            cnt = 0
            for i in range(N):
                for j in range(M):
                    # 전체 빈칸 카운팅
                    if lab[i][j] == 0:
                        cnt +=1
            if cnt > max_safe_area:
                max_safe_area = cnt
            # 바이러스 초기화
            for i in range(N):
                for j in range(M):
                    if lab[i][j] == 2 and not (i,j) in virus_location:
                        lab[i][j] = 0
            # 벽 허물기
            lab[w1_y][w1_x] = 0
            lab[w2_y][w2_x] = 0
            lab[w3_y][w3_x] = 0
            
print(max_safe_area)



# 특정영역의 카운팅인지 전체 영역 카운팅인지 생각하기
# 함수가 이상하게 작동하면 들여쓰기 확인해보기
# 순열과 조합 구현 공부하기
# 같은 그래프에서 탐색을 여러번 하는 경우에는 복사본을 이용하기
# 안전 영역을 구하는건 그냥 전체 탐색을 해도 됨