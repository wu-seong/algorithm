'''
모든 수에 -1씩 하는데
연속해서 0이하가 되는 구간이 k 초과일 때를 구하는 것

길이가 k인 구간 중에서 가장 최댓값이 낮은 구간을 찾고 그 최댓값

첫 구간 카운팅

'''
from heapq import heapify, heappush, heappop
from collections import defaultdict
def solution(stones, k):
    n = len(stones)
    heap = list(map(lambda x: x*-1, stones[0:k]))
    count = defaultdict(int)
    heapify(heap)
    min_result = -heap[0]
    for v in stones[0:k]:
        count[v] += 1
    #print(count)
    for i in range(n-k):
        #print(heap)
        count[stones[i]] -= 1 
        # 뺄 값이 최댓값이면 pop
        if stones[i] == -heap[0]:
            heappop(heap)
            while heap and not count[-heap[0]]: # 이전에 삭제 됐었다면
                heappop(heap)
                
        # 다음값 heap에 push
        heappush(heap,-stones[i+k])
        count[stones[i+k]] += 1
        # 최댓값 읽어서 최소 비교
        min_result = min(min_result, -heap[0])
    #print(min_result)
    return min_result