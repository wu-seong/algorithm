import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
'''
낮은 곳으로 dfs하기
그런데 이미 방문한 곳이면
dfs하는 것이 아니라 목적지 까지의 경우의 수 * 


다음이 목적지이면 + 1
목적지가 아니면 다음의 경우의 수를 현재에 더하기
목적지가 아니고 안 가본곳이면 재귀
목적지가 아니고 가본 곳이면 그대로 더하기

dfs함수
그래프를 미리 만들기

'''

from collections import defaultdict
def solution(n, m, nnap):
  graph = defaultdict(list)
  dp = [[-1 for _ in range(m)] for _ in range(n)]

  def set_next(y,x):
    nonlocal graph
    for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
      yy, xx = y + dy, x + dx
      if 0 <= yy < n and 0 <= xx < m and nnap[yy][xx] < nnap[y][x]:
        graph[(y,x)].append((yy,xx))
  def set_graph():
    for i in range(n):
      for j in range(m):
        set_next(i,j)
  set_graph()
  #print(graph)

  def dfs(cur):
    nonlocal nnap
    y,x = cur
    if (y,x) == (n-1, m-1): # 도착지점의 경우
      return 1
    sum = 0
    #print(len(graph[(y,x)]))
    if len(graph[(y,x)]) == 0: # 갈 곳이 없을 경우
      dp[y][x] = 0
      return 0
    for next in graph[(y,x)]:
      yy,xx = next
      if dp[yy][xx] == -1: # 안 가본 경우
        sum += dfs(next)
      else:
        sum += dp[yy][xx]
    dp[y][x] = sum
    return sum
  dfs((0,0))
  print(dp[0][0])

n,m = map(int, input().rstrip().split())
nnap = []
for _ in range(n):
  nnap.append(list(map(int, (input().rstrip().split()))))
#print(nnap)
solution(n,m, nnap)
'''
3 3
9 8 7
6 5 4
3 2 1
'''