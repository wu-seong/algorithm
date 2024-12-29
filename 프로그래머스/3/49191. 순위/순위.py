
'''
플로이드 와샬을 이용해서 모든 노드간 참조 가능을 판단하기
각 노드 마다 winner or loser 관계로 연결

중간 노드가 출발 노드의 winner이고 도착 노드의 loser이면
출발 노드의 winner에 도착 노드를 추가
도착 노드의 loser에 출발 노드를 추가

반대의 경우도 마찬가지
'''

from collections import defaultdict
def solution(n, results):
    dist = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for winner, loser in results:
        dist[winner][loser] = 1
        dist[loser][winner] = -1
    #print(dist)
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if dist[i][k] == -1 and dist[k][j] == -1:
                    dist[i][j] = -1
                    dist[j][i] = 1
                elif dist[i][k] == 1 and dist[k][j] == 1:
                    dist[i][j] = 1
                    dist[j][i] = -1
    # 0이 아닌 것의 개수
    result = 0
    for edges in dist:
        cnt = 0
        for edge in edges:
            if edge:
                cnt += 1
        if cnt == n-1:
            result += 1
    #print(dist)
    #print(result)
    return result