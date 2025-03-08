'''

이미 방문한 visited 노드
다음 방문할 수 있는 next 노드

자식노드들 next 노드에 추가 -> 방문체크 -> 방문하지 않은 것 재귀(조건 고려해서) -> 자식 노드 next노드에서 제거
 
'''
import sys
sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
def solution(info, edges):
    n = len(info)
    tree = [[] for _ in range(n)]
    for p, c in edges:
        tree[p].append(c)
    #print(tree)
    result = 0
    def dfs(cur, sheep, wolf, next, visited):
        nonlocal result
        #print('현재노드:', cur, '양/늑대: ', sheep, wolf)
        # 최댓값 갱신
        result = max(result, sheep)

        # 자식노드 next에 추가
        next.update(set(tree[cur]))
        #print('다음에 방문할 노드', next)
        for c in next:
            if info[c]: # 늑대이고 잡아먹히진 않으면 방문하기
                if sheep > wolf + 1 and not c in visited:
                    visited.add(c)
                    dfs(c,sheep,wolf+1, next.copy(), visited.copy())
                    visited.remove(c)
            else: # 양이면 방문 리스트에 추가
                if not c in visited:
                    visited.add(c)
                    dfs(c,sheep+1,wolf, next.copy(), visited.copy())
                    visited.remove(c)
        next.difference_update(set(tree[cur]))
    dfs(0,1,0,set(),set())
    return result
    
                
        
        
