'''
자식의 가중치 + 자식의 길이 중에서 가장 크기가 큰 것 2개의 합

dfs로 구하기

부모, 자식, 가중치
입력 받아서 그래프 정보 만들기


'''
import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
input = sys.stdin.readline

n = int(input().rstrip())

graph = defaultdict(list)
for _ in range(n-1):
    p, c, w = map(int, input().rstrip().split())
    graph[p].append((c,w))
#print(graph)

result = 0
def dfs(current):
    global result
    # 리프노드이면 0 반환
    if len(graph[current]) == 0:
        return 0
    # 자식 중 가장 큰 것(재귀) + 가중치 구하기 

    lengths = [0]
    for c, w in graph[current]:
        l = dfs(c) + w
        lengths.append(l)
    lengths.sort(reverse=True)
    # 그 중에서 합이 가장 큰 2개를 구해서 최댓값 갱신
    result = max(result, lengths[0] + lengths[1])
    # 반환은 가장 큰 것 1개만
    return lengths[0]
dfs(1)
print(result)