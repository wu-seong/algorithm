'''
비선점, 짧은 것, 빠른 것, 번호 순

시작순으로 오름차순 정렬

일단 첫 시작은 가장 빠른 것 부터 시작
종료시간(시작 + 경과)이 되면 
종료시간 이하까지 힙에 넣기, 힙에 넣을 때는 짧,빠,번

만약 힙에 넣을 것이 없으면 그 다음 작업을 힙에 넣음

힙에 작업이 없을 때 까지
'''
from heapq import heappush, heappop
def solution(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    print(jobs)
    heap = []
    i = 0
    heappush(heap, (jobs[0][1], jobs[0][0]))
    i += 1
    time = jobs[0][0]
    times = []
    while heap:
        #print(heap)
        w_time, r_time = heappop(heap)
        # 시간 작업
        time += w_time
        times.append(time - r_time)
        #print(time)
        while i < n and jobs[i][0] <= time: # 요청시간 된 얘들 작업 큐에 넣기
            heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
            check = False
        if not heap and i < n: # 바로 이어서 작업하지 않으면 다음 요청
            heappush(heap, (jobs[i][1], jobs[i][0]))
            time = jobs[i][0]
            i += 1
    print(times)
    return sum(times) // n
    
    
    
    
    