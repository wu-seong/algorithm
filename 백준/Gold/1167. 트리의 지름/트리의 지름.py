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

graph = defaultdict(set)
nums = list(map(int, input().rstrip().split()))
root = nums[0]
for i in range(1, len(nums), 2):
    if nums[i] != -1:
        graph[root].add((nums[i], nums[i+1]))

for _ in range(n-1):
    nums = list(map(int, input().rstrip().split()))
    for i in range(1, len(nums), 2):
        if nums[i] != -1:
            graph[nums[0]].add((nums[i], nums[i+1]))
            graph[nums[i]].add((nums[0], nums[i+1]))

#print(graph)

visited = set()
result = 0
def dfs(current):
    global result
    # 리프노드이면 0 반환
    if len(graph[current]) == 0:
        return 0
    # 자식 중 가장 큰 것(재귀) + 가중치 구하기 

    lengths = [0,0]
    for c, w in graph[current]:
        if not c in visited:
            visited.add(c)
            l = dfs(c) + w
            lengths.append(l)
    lengths.sort(reverse=True)
    # 그 중에서 합이 가장 큰 2개를 구해서 최댓값 갱신
    result = max(result, lengths[0] + lengths[1])
    # 반환은 가장 큰 것 1개만
    return lengths[0]
visited.add(root)
dfs(root)
print(result)