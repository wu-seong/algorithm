'''
처음에 테두리를 구하기
지게차 -> 테두리와 인접한 대상 컨테이너 없애기
크레인 -> 그냥 모든 대상 컨테이너 찾아 없애기
모든 테두리를 순회하면서 빈 곳이 있으면 dfs하여 테두리 갱신하기
빈 곳이 없으면 바로 pass

'''
from collections import deque
def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    for i in range(n):
        storage[i] = deque(storage[i])
    storage = deque(storage)

    for i in range(n):
        storage[i].append('1')
        storage[i].appendleft('1')
    storage.append(deque(['1' for _ in range(m+2)]))
    storage.appendleft(deque(['1' for _ in range(m+2)]))
    #print(storage)
    remove_list = [] # 이번 사이클에 제거한 목록
    def find_adjust(target): # 해당하는 컨테이너 찾아서 제거하기
        nonlocal storage, remove_list
        # 테두리와 인접한 것 제거
        for i in range(n+2):
            for j in range(m+2):
                if storage[i][j] == '1': # 테두리 이면 인접한 것 제거
                    for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                        ii = i + di
                        jj = j + dj
                        if 0 <= ii < n+2 and 0 <= jj < m+2 and storage[ii][jj] == target:
                            storage[ii][jj] = '0' # 제거된 것 표시
                            remove_list.append((ii,jj))
                            
    #find_adjust('A')
    def find_all(target):
        find_adjust(target)
        for i in range(n+2):
            for j in range(m+2):
                if storage[i][j] == target:
                    storage[i][j] = '0'
#     find_all('A')
#     for s in storage:
#         print(s)
        
    def transfer(cur):
        nonlocal storage
        i,j = cur
        storage[i][j] = '1'
        for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
            ii = i + di
            jj = j + dj
            if 0 <= ii < n+2 and 0 <= jj < m+2 and storage[ii][jj] == '0':
                transfer((ii,jj))
    # print()
    # for s in storage:
    #     print(s)
    for request in requests:
        target = request[0]
        if len(request) == 1:
            find_adjust(target)
        else:
            find_all(target)
        for r in remove_list:
            transfer(r)
        
    print()
    # for s in storage:
    #     print(s)
    cnt = 0
    for i in range(n+2):
        for j in range(m+2):
            if storage[i][j].isalpha():
                cnt += 1
    #print(cnt)
    return cnt
                
    
        
        
    