import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    '''
    2차원 배열 통해서 그래프 정보 완성하기
    
    y값 기준으로 
    y값 순서대로 내림차순 정렬시키기
    x값을 각 level별로 넣기
    
    루트 노드는 자식과 모두 연결하기
    줄기 노드는 부모의 x값 보다 작은 것들과 큰 것들 구분해서 
    
    자식 노드를 연결한 뒤 재귀
    왼쪽 오른쪽 리미터를 정하기
    왼쪽 ~ 오른쪽 사이의 노드는 모두 본인과 연결
    다시 재귀 호출 시 왼쪽 ~ 본인, 본인 ~ 오른쪽 으로 재귀 탐색하기
    
    
    완성한 그래프 정보를 루트 노드를 시작점으로 전위 순회, 후위 순회한 결과를 찾기
    '''
    
    from collections import defaultdict
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    #print(nodeinfo)
    nodeinfo.sort(reverse=True, key=lambda x: (x[1], -x[0]))
    #print(nodeinfo)
    
    n = len(nodeinfo)
    nodes = [[] for _ in range(n)] 
    pre_y = nodeinfo[0][1]
    l = 0
    for node in nodeinfo:
        x,y,v = node
        if y < pre_y:
            l += 1
        pre_y = y
        nodes[l].append((v, x))
    nodes = nodes[:l+1]
    root = nodes[0][0]
    #print(root)
    depth = len(nodes)
    graph = defaultdict(list)
    
    def connect(level, current, left, right):
        v,x = current
        #print(left, x, right)
        if level == depth-1:
            return
        # 연결하기
        for child in nodes[level+1]:
            c_v, c_x = child
            if left <= c_x < right:
                graph[v].append(c_v)
                if c_x < x:
                    connect(level+1, child, left, x)
                else:
                    connect(level+1, child, x+1, right)
    connect(0, root, 0, 100001)
    #print(graph)
    
    pre_result, post_result = [], []
    def prefix(current):
        nonlocal pre_result
        pre_result.append(current)
        for child in graph[current]:
            prefix(child)
    prefix(root[0])
    
    def postfix(current):
        nonlocal post_result
        for child in graph[current]:
            postfix(child)
        post_result.append(current)
    postfix(root[0])
    #print(pre_result, post_result)
    return [pre_result, post_result]
    
    
        
    
        
        