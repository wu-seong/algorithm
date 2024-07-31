import sys
input = sys.stdin.readline

min_cost = float('inf')

def dfs(start, node, visited, current_sum, depth):
    global N, W, min_cost
    # 모든 노드를 방문하고 시작 노드로 돌아오면 비용 비교
    if depth == N - 1 and W[node][start] != 0:
        current_sum += W[node][start]
        if min_cost > current_sum:
            min_cost = current_sum
        return

    for i in range(N):
        if W[node][i] != 0 and not visited[i]:
            visited[i] = True
            dfs(start, i, visited, current_sum + W[node][i], depth + 1)
            visited[i] = False

N = int(input())

W = [list(map(int, input().rstrip().split())) for _ in range(N)]

visited = [False for _ in range(N)]
visited[0] = True
dfs(0, 0, visited, 0, 0)

print(min_cost)
