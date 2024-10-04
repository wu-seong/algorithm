from collections import deque

def solution(people, limit):
    # 정렬
    people.sort()
    people = deque(people)
    cnt = 0
    # 가장 무거운 사람과 가장 가벼운 사람의 합이 <= limit 이면 같이 탈출 아니면 뒤에사람만 혼자 탈출
    while people:
        if len(people) == 1:
            cnt += 1
            break
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        else:
            people.pop()
        cnt += 1
    #print(cnt)
    return cnt