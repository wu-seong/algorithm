import sys
sys.setrecursionlimit(10**6)

def solution(land):
    n, m = len(land), len(land[0])
    area = [[0] * m for _ in range(n)]  # 각 위치의 석유량 저장
    oil_sizes = {}  # {영역 ID: 석유량} 저장

    def dfs(y, x, area_id):
        stack = [(y, x)]
        cells = []
        while stack:
            cy, cx = stack.pop()
            if area[cy][cx] == 0:  # 방문하지 않은 경우만 탐색
                area[cy][cx] = area_id  # 같은 영역 ID로 마킹
                cells.append((cy, cx))
                for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < n and 0 <= nx < m and land[ny][nx] and area[ny][nx] == 0:
                        stack.append((ny, nx))
        
        oil_sizes[area_id] = len(cells)  # 현재 영역의 총 석유량 저장

    # Step 1: 모든 영역에 대해 DFS 수행하여 석유량 계산
    area_id = 1  # 1부터 시작하여 각 영역을 구분
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and area[i][j] == 0:
                dfs(i, j, area_id)
                area_id += 1

    # Step 2: 각 열(column)별로 석유량 계산
    max_oil = 0
    for x in range(m):
        seen_areas = set()
        total_oil = 0
        for y in range(n):
            if area[y][x] > 0 and area[y][x] not in seen_areas:
                seen_areas.add(area[y][x])
                total_oil += oil_sizes[area[y][x]]
        max_oil = max(max_oil, total_oil)

    return max_oil
