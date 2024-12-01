import heapq
def solution(n, works):
    '''
    모두 heap에 넣기
    pop해서 다음 pop할 것과 차이 구하기
    차이가 0이면 1뺀 것 push, (0이면 push 안함)
    n에서 그 차이만큼을 빼고, 뺀 만큼의 값을 push하기 (n이 충분할 때, n >= distance)
    n이 차이보다 더 작으면 pop에서 n만큼만 뺀 것을 push하기
    
    n이 0이 될 때 까지 반복 or works가 없을 때 까지 반복
    '''
    
    # 모두 heap에 넣기
    works = [-n for n in works]
    heapq.heapify(works)
    while n > 0 and works:
        #print(n, works)
        cur = -heapq.heappop(works)
        if works:
            next = -works[0]
            #print(cur, next)
            dist = abs(next - cur)
            if dist: # 차이가 있으면
                if n >= dist: # n이 충분할 때
                    n -= dist
                    heapq.heappush(works, -next)
                else: # n이 부족할 때
                    heapq.heappush(works, -(cur - n))
                    n = 0
            else: # 차이가 없으면
                if next - 1: # 1씩 작업해도 작업이 남는다면
                    heapq.heappush(works, -(next - 1))
                n -= 1
        else: # 남은 작업이 없으면 0 리턴
            return 0
    #print("결과", works)
    sum = 0
    for n in works:
        sum += n**2
    return sum
                