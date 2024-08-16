from collections import deque
def solution(n, computers):
    
    visited = [ False for _ in range(n)]
    queue = deque()
    
    cnt = 0
    #bfs 하면서 카운팅
    for i in range(n):
        # 아직 방문하지 않은 노드가 있다면 카운팅 하고 노드 순회
        if not visited[i]:
            cnt += 1
            visited[i] = True
            queue.append(i)
            while queue:
                a = queue.popleft()
                for j in range(n):
                    # 방문하지 않았고, 방문가능 하다면 방문
                    if not visited[j] and computers[a][j] == 1:
                        visited[j] = True
                        # 같은 노드로는 방문 표시만
                        if j == a:
                            continue
                        queue.append(j)
    answer = cnt
    return answer
