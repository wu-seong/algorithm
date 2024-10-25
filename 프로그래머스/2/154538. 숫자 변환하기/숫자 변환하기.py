from collections import deque
def solution(x, y, n):
    # +n *2 *3
    # bfs?
    
    visited = [False] * (y+1)
    q = deque()
    q.append((x,0))
    visited[x] = True
    while q:
        num, cnt = q.popleft()
        #print(num,cnt)
        if num == y:
            return cnt
        next_num = [num + n, 2*num, 3*num]
        for xx in next_num:
            if xx <= y and not visited[xx]:
                visited[xx] = True
                q.append((xx,cnt+1))
    return -1
            
            
    
    