from heapq import *
def solution(n, k, enemy):
    '''
    무적권 x -> 부활권 (더 작아질 때 지금까지 상대했던 적 중 큰 수 만큼 더하기, 현재 포함)
    부활권이 없으면 거기까지가 최종 라운드
    '''
    
    length = len(enemy)
    heap = []
    for i in range(length):
        #print( n - enemy[i])
        if n - enemy[i] < 0: # 못막을 시
            heappush(heap, -enemy[i])
            while heap and k > 0 and n - enemy[i] < 0: # 부활권 남아있고 아직 못막을 시에 부활권 사용하기
                #print(heap, n, k)
                n += -heappop(heap)
                k -= 1
            n -= enemy[i]
            if n < 0: # 못막는 경우
                return i
        else:
            n -= enemy[i]
            heappush(heap, -enemy[i])
    return length
                
        