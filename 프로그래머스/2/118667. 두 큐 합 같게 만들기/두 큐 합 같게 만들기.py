from copy import deepcopy
from collections import deque
def solution(queue1, queue2):
    # 합이 더 작은 쪽에 주기
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    o_queue1 = deepcopy(queue1)
    o_queue2 = deepcopy(queue2)
    sum1 = sum(o_queue1)
    sum2 = sum(o_queue2)
    du_set = set()
    du_set.add((sum1,sum2))
    cnt = 0
    n = len(queue1) + len(queue2)
    i = 0
    while i <= n * 2:
        if sum1 == sum2:
            return cnt
        if sum1 > sum2:
            value = queue1.popleft()
            queue2.append(value)
            sum1 -= value
            sum2 += value
        else:
            value = queue2.popleft()
            queue1.append(value)
            sum2 -= value
            sum1 += value
        cnt += 1
        i += 1
    return -1
        