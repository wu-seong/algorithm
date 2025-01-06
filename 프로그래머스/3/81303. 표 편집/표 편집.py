'''
아니 X의 합이 100만 이하인 조건이 있었네
-> 총 move의 횟수가 100만 이하라는 거

그럼 그냥 링크드리스트로 구현하면 됨;;

이전, 다음 인덱스 기록하기

C가 오기 전까지는
D, U에 계산하기

C가 오면 
계산된 횟수만큼 링크 N번 타서 이동하기
1. 삭제할 노드에 X표시하기
2. 삭제할 노드 stack에 넣기
3. 삭제할 얘를 참조하는 링크를 이어주기 (뒤는 앞걸로, 앞은 뒤걸로)
'''
def solution(n, k, cmd):
    stack = []
    linked_list = [None for _ in range(n)]
    for i in range(n):
        linked_list[i] = [i]
        if i > 0: # 이전 노드
            linked_list[i].append(i-1)
        else:
            linked_list[i].append(-1)
        if i < n-1: # 다음 노드
            linked_list[i].append(i+1)
        else:
            linked_list[i].append(-1)
        linked_list[i].append('O')
    #print(linked_list)
    
    cur = linked_list[k]
    #print(cur)
    for s in cmd:
        # for l in linked_list:
        #     print(l)
        # print('cmd: ', s ,'\ncur: ', cur[0])
        if s == 'C':
            # 삭제 표시하고 참조하던 인접노드와 같이 stack에 넣기
            cur[3] = 'X'
            stack.append(cur)
            
            # 참조 끊기
            if cur[1] != -1:
                linked_list[cur[1]][2] = cur[2]
            if cur[2] != -1:
                linked_list[cur[2]][1] = cur[1]
            # 한칸 뒤로 이동
            if cur[2] != -1:
                cur = linked_list[cur[2]]
            else:
                cur = linked_list[cur[1]]
        
        elif s == 'Z':
            # 복구
            node = stack.pop()
            node[3] = 'O'
            if node[1] != -1:
                linked_list[node[1]][2] = node[0]
            if node[2] != -1:
                linked_list[node[2]][1] = node[0]
        else:
            c, cnt = s.split(" ")
            cnt = abs(int(cnt))
            for _ in range(cnt):
                if c == 'D':
                    cur = linked_list[cur[2]]
                else:
                    cur = linked_list[cur[1]]
            
    #     print('\nsum: ', sum)
    # print(linked_list)
    result = []
    for l in linked_list:
        result.append(l[3])
    return ''.join(result)
    