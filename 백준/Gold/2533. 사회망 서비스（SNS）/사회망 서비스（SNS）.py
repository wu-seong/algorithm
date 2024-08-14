import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 현재 선택한 노드의 최소 얼리 어댑터 수 = 각 자식노드의 최소 얼리 어댑터 수의 합

# 자식이 없다면 최소 얼리 어댑터 수는 0개(부모가 얼리 어댑터면 되니까), 자식은 일반인
# 자식이 있다면 자식의 얼리 어댑터 수의 합
# 자식 중 얼리 어댑터가 아닌 것이 있다면 부모가 얼리 어댑터가 됨

def dfs(root):
    # 자식 최소 얼리 어댑터 수 구하기
    sum = 0
    # leaf node
    if not graph[root]:
        dp[root] = 0
        return

    for n in graph[root]:
        # 안구했으면 방문하지 않은 곳으로 재귀
        if not visited[n]:
            visited[n] = True
            graph[n].remove(root)
            dfs(n)
        sum += dp[n]
        # 자식 중 리프노드가 있다면 현재 노드는 얼리어뎁터
        if not adp[n]:
            adp[root] = True

    if adp[root]:
        sum += 1
    dp[root] = sum

N = int(input().rstrip())
graph = [ [] for _ in range(N+1)]
# 각 노드 마다 엣지 정보 저징
for i in range(N-1):
    u,v = map(int,input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# 각 노드가 루트 노드가 되어 최소 어댑터 수 저장
dp = [-1] * (N+1)
visited = [False] * (N+1)
visited[1] = True

adp = [False] * (N+1)
dfs(1)
print(dp[1])


# 어떤 도착지에 확실히 방문을 해서 데이터를 쌓아나가야 한다면 dfs