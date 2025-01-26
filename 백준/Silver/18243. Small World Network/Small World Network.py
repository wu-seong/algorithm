import sys
input = sys.stdin.readline
from collections import deque
'''
모든 정점을 시작점으로 해서 BFS를 돌려서 6이하인지를 판단한다.
하나라도 6을 넘어서면 Big world이다.

1. N, K의 값을 받아서 그래프 정보를 만든다.(양방향)
2. 각 노드를 순회하면서 BFS탐색을 한다.
    탐색시에 6번째 탐색시에 visited의 길이가 N미만이면 Big world이다.
    모든 노드에 대해서 6번째 level 안에 탐색이 끝나면 Small World이다.
'''

N, K = map(int, (input().rstrip().split()))
graph = [[] for _ in range(N+1)]
#print(graph)
for _ in range(K):
    n1, n2 = map(int, (input().rstrip().split()))
    graph[n1].append(n2)
    graph[n2].append(n1)

def is_big(start):
    visited = set()
    q = deque()

    visited.add(start)
    q.append((start, 1))
    while q:
        current, cnt = q.popleft()
        #print("current: ", current, "cnt: ", cnt)
        if cnt == 7:
            break
        for next in graph[current]:
            if not next in visited:
                visited.add(next)
                q.append((next, cnt + 1))
    # 6단계까지 방문을 마쳤는데 모든 노드를 방문하지 못한 경우
    if len(visited) < N:
        return True
    return False
for i in range(1, N+1):
    if is_big(i):
        print("Big World!")
        exit()
print("Small World!")