from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip().split())
# 그래프 정보 만들기
graph = [ [] for _ in range(N+1)]
for _ in range(M):
    s,d = map(int, input().rstrip().split())
    graph[s].append(d)
    graph[d].append(s)
#print(graph) 
# 각 사람마다 케빈 - 베이컨 수 구하기
cnt = [0] * (N+1)
for i in range(1,N+1):
    # BFS 하여 각 사람당 거리 구하여 합산
    visited = set()
    queue = deque()
    visited.add(i)
    queue.append((i,0))
    while queue:
        node, level = queue.popleft()
        for next in graph[node]:
            if not next in visited:
                visited.add(next)
                cnt[i] += (level+1)
                queue.append((next, level+1))    
#print(cnt)
min_cnt = float('inf')
min_idx = 0
for i in range(1,N+1):
    if min_cnt > cnt[i]:
        min_cnt = cnt[i]
        min_idx = i
print(min_idx)

