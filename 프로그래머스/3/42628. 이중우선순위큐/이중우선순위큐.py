from collections import defaultdict
from heapq import heappop, heappush


counter = defaultdict(int)
max_heap, min_heap = [], []

def parse(command):
    c, num = command.split(" ")
    num = int(num)
    if c == 'I':
        counter[num] += 1
        heappush(max_heap, -num)
        heappush(min_heap, num) 
    else:
        # 최댓값 삭제
        if num == 1:
            while max_heap:
                removed = heappop(max_heap)
                # 존재하면 삭제 카운팅, 아니면 존재하는 것 끝까지 찾기
                if counter[-removed] > 0:
                    counter[-removed] -= 1
                    break
        # 최솟값 삭제
        else:
             while min_heap:
                removed = heappop(min_heap)
                # 존재하면 삭제 카운팅, 아니면 존재하는 것 끝까지 찾기
                if counter[removed] > 0:
                    counter[removed] -= 1
                    break
    #print(max_heap, min_heap, counter)
        
def solution(operations):
    '''
    Counter를 두어
    Insert 시에 개수 ++
    pop 시에 개수 --
    
    지우려고 하는 값의 개수가 0이 아닐 때 까지 pop 하기
    그러다가 heap이 empty이면 끝
    
    최댓값: 최대 힙에서 유효한 녀석 구하기
    최솟값: 최소 힙에서 유효한 녀석 구하기
    '''
    for o in operations:
        parse(o)
    
    max_result, min_result = 0,0
    while max_heap:
        popped = heappop(max_heap)
        if counter[-popped] > 0:
            max_result = -popped
            break
    while min_heap:
        popped = heappop(min_heap)
        if counter[popped] > 0:
            min_result = popped
            break
    return [max_result, min_result]