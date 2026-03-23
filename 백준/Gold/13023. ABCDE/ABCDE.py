'''
5명이 있으면
A <-> B <-> C <-> D <-> E

이 관계가 있는지를 구해야함


0 <-> 1 <-> 2 <-> 3 <-> 0 
-----4

1 <-> 7 <-> 4
      3
dfs로 탐색해서 depth가 4인 경우가 1번이라도 있으면 1

# 시간복잡도 (2000 + 2000) = O(4000)
# 변수
인접 그래프: int 2차원 배열 
방문 표시 : set<int>
'''

import sys

input = sys.stdin.readline

n,m = list(map(int, input().rstrip().split(" ")))

graph = [ [] for _ in range(n)]
visited = set()
#print(graph)

def dfs(x, depth):
  # 다음 방문할 곳 순회하기
  # 방문하지 않은 곳만 방문하기
  if depth == 4:
    print(1)
    exit()
  for nx in graph[x]:
    if not nx in visited:
      visited.add(nx)
      dfs(nx, depth + 1)
      visited.remove(nx)

for _ in range(m):
  a,b = map(int, input().rstrip().split(" "))
  # 그래프 만들기
  graph[a].append(b)
  graph[b].append(a)
#print(graph)
# 하나라도 dfs의 깊이가 4에 도달하는것이 있으면 1

for i in range(n):
  # 방문 초기화
  #visited = set()
  # dfs
  visited.add(i)
  dfs(i, 0)
  visited.remove(i)

print(0)





