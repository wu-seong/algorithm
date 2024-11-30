from collections import defaultdict
import heapq
def solution(operations):
    '''
    최소 힙이라고 생각하고 
    D -1 은 가능 
    만약 현재 힙 길이가 1이라면 D 1은 D -1과 같음
    그렇지 않으면 D 1은 나중에 수행해도 됨?

    만약 D -1을 하고 나서 길이가 나중에 D 1 을 수행할 원소를 침범할 경우
    그러니까 그냥 D 1이 됐다고 '가정' 하는거임
    
    -> D 1을 할 때마다 카운팅 하여 실제 힙 길이 - count 를하여 0이면 카운팅 초기화
    -> D 1을 할 때와 D -1을 할 때 마다 확인하기
    -> 마지막에는 남은 카운팅만큼 실제로 최대 힙을 만들어서 자르기
    
    
    최대힙, 최소힙 두 개를 만들어서 이용
    삽입 시에는 두 힙에 모두 삽입
    하지만 삭제 시에는 D 1 이면 최대힙에서, D -1 이면 최소힙에서 삭제
    그런데 최대 힙에서 삭제 한 것이 최소힙에서는 반영이 안되니 삭제한 리스트를 관리하기
    각 원소 마다 0으로 하여 삽입 시에 + 1 삭제 시에 -1 하여 삭제하려는 원소가 이미 0이면 양수인 원소가 나올 때 까지 pop, 만약 pop할 원소가 없으면 pass
    
    '''
    min_heap = []
    max_heap = []
    counter = defaultdict(int)
    for op in operations:
        if op[0] == 'I':
            _, num = op.split(" ")
            num = int(num)
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            counter[num] += 1
        else:
            if op[2] == '-': # 최솟값 삭제
                while min_heap:
                    remove_num = heapq.heappop(min_heap)
                    if counter[remove_num]: # 1이상이면
                        counter[remove_num] -= 1
                        break
            else:
                while max_heap:
                    remove_num = -heapq.heappop(max_heap)
                    if counter[remove_num]: # 1이상이면
                        counter[remove_num] -= 1
                        break
    min_result = 0
    while min_heap: # counter에 1 이상인 얘를 반환
        min_num = heapq.heappop(min_heap)
        if counter[min_num]: # 1이상이면
            min_result = min_num
            break
    else:
        return [0,0]
    
    max_result = 0
    while max_heap: # counter에 1 이상인 얘를 반환
        max_num = -heapq.heappop(max_heap)
        if counter[max_num]: # 1이상이면
            max_result = max_num
            break
    return [max_result, min_result]
        
