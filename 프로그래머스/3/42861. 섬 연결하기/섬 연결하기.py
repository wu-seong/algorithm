'''
다리의 가중치가 적은 것 순으로 연결
이미 방문한 다리면 패스하기
모든 노드가 이어질때까지인데
모든 노드가 이어짐을 어떻게 판단?
유니온 파인드
'''
def solution(n, costs):
    if n == 1:
        return 0
    # 유니온 파인드 루트노드 초기화
    parent = [i for i in range(n)]
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x] 
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootX] = parent[rootY]
            return True
        return False
    
    costs.sort(key=lambda x:x[2])
    result = 0
    print(costs)
    for s, e, c in costs:
        if union(s,e):
            result += c
    print(result)
    return result

'''
tc
1. 섬이 1개
2. costs 중간에 끝나는 경우
3. 가중치가 똑같은 경우
'''
  