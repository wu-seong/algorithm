import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())

    # 노드 정보 딕셔너리에 저장
    graph = {}
    start_x, start_y = map(int, input().rstrip().split())
    graph[(start_x, start_y)] = []

    for _ in range(n):
        graph[tuple(map(int, input().rstrip().split()))] = []

    dst_x, dst_y = map(int, input().rstrip().split())
    graph[(dst_x, dst_y)] = []

    # 각 노드마다 연결 가능한 엣지 연결 (맨헤튼 거리 <= 1000)
    for node1 in graph.keys():
        for node2 in graph.keys():
            if node1 == node2:
                continue
            distance = abs(node2[0] - node1[0]) + abs(node2[1] - node1[1])
            if distance <= 1000:
                graph[node1].append(node2)
                

    #print(graph)
    # 연결한 그래프 정보로 너비 우선 탐색
    visited = set()
    queue = deque()
    root = (start_x, start_y)
    queue.append(root)
    visited.add(root)
    
    success = False
    while queue:
        coordinates = queue.popleft()
        if coordinates == (dst_x, dst_y):
            print("happy")
            success = True
            break
        for node in graph[coordinates]:
            if not node in visited:
                visited.add(node)
                queue.append(node)
    if not success:
        print("sad")
    
    