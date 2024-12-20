'''
첫번째로 도달한 것이 최소 경로가 아니므로 bfs는 안됨

다익?
그냥 갈 때는 1인데 코너를 돌면 5
이전 노드와 이 다음 노드의 x,y중 다른 것이 하나라도 있다면 코너

'''
from collections import defaultdict
from heapq import heappush, heappop
def solution(board):
    n = len(board)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    dist[0][0] = 0
    result = float('inf')
    def dijkstra(start):
        nonlocal result, dist
        q = []
        y,x = start
        heappush(q, (0,y,x,0,y,x)) # 직선이 우선 직선:0 꺾은선: 1
        while q:
            _, y,x,w,p_y,p_x = heappop(q)
            
            if (y,x) == (n-1,n-1):
                result = min(result, w)
                continue
            
            # 만약 더 긴 경로라면
            if dist[y][x] + 5 < w:
                # 더 긴 경로이지만 다음목적지를 직선으로 간다면
                # + 5 안쪽으로 더 긴 경로이면 고려하기??
                continue
            #print(y,x,dist[y][x], w, "\n", dist)
            # 다음 갈 노드 힙에 추가
            for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
                yy = y + dy
                xx = x + dx
                if 0 <= yy < n and 0 <= xx < n and not board[yy][xx]:
                    #print(p_y, p_x, yy, xx)
                    if p_y != yy and p_x != xx:
                        if dist[y][x] + 6 <= dist[yy][xx]:
                            dist[yy][xx] = dist[y][x] + 6
                            heappush(q, (1,yy,xx,w+6,y,x))
                    else:
                        if dist[y][x] + 1 <= dist[yy][xx]:
                            dist[yy][xx] = dist[y][x] + 1
                            heappush(q, (0,yy,xx,w+1,y,x))
                            
    dijkstra((0,0))
    print(dist, result)
    return result * 100
    
    

                
    
  