from collections import deque
def solution(priorities, location):
    # 큐를 구현해서 시뮬
    # n*n <= 10000
    # 계속 큐에서 왔다갔다 하니 번호 지정해놓기
    priorities = [(i,v) for i,v in enumerate(priorities)]
    # print(priorities)
    # deque하기
    # 우선순위 비교해서 더 높은 것이 없으면 실행하기 == 실행 카운팅 (찾는 인덱스면 카운팅 반환)
    # 있으면 다시 큐에 넣기
    # 큐가 빌 때 까지
    q = deque(priorities)
    cnt = 0
    while q:
        num = q.popleft()
        can_process = True 
        for i,v in q: # 순회하면서 하나라도 더 높으면 다시 넣기
            if v > num[1]:
                q.append(num)
                can_process = False
                break
        if can_process:
            cnt += 1
            if num[0] == location:
                return cnt
    