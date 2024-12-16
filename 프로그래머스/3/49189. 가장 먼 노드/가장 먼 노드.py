'''
bfs하면서 각 level에 도달한 node의 개수 구하기

'''
from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    #print(graph)
    visited = set()
    count = [0] * (n+1)
    def bfs():
        q = deque()
        q.append((1, 0))
        visited.add(1)
        # for문 돌면서 다음 갈 곳 queue에 넣기
        while q:
            current, level = q.popleft()
            count[level] += 1
            for next in graph[current]:
                if not next in visited:
                    q.append((next, level+1))
                    visited.add(next)
    bfs()
    result = 0
    for i in range(n):
        if count[i]:
            result = count[i]
    print(result)
    return result
        