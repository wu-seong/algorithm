from heapq import heappop, heappush, heapify
def solution(n, works):
    '''
    제곱은 큰 숫자에서 값이 클수록 늘어난다.
    가장 작업량이 높은 work부터 줄인다.
    works를 최대힙으로 만든다.
    pop하고 1씩 줄인 것을 push한다
    위를 n번 반복한다.
    '''
    # 최대 heap만들기
    for i in range(len(works)):
        works[i] = -works[i]
    heapify(works)
    #print(works)
    # 큰 것 부터 일 하기
    i = n
    while works and i > 0:
        value = -heappop(works)
        if value - 1 != 0:
            heappush(works, -(value - 1))
        i -= 1
    print(works)
    # 피로도 구하기
    result = 0
    for p in works:
        result += (p ** 2)
    return result
    