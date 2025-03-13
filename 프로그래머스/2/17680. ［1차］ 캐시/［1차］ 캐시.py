'''
가장 나중것이 먼저 사라지는 알고리즘 -> 큐로 밀어내기

큐에 있는지를 먼저 확인
있다면 삭제하고 새로 넣기

없으면
    가득 차있으면 하나를 빼고 넣기
    그렇지 않으면 넣지 않음
'''
from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    for i, city in enumerate(cities):
        cities[i] = city.lower()
    #print(cities)
    cache_queue = deque([])
    result = 0
    def cache(city):
        nonlocal result, cache_queue
        # hit
        if city in cache_queue: 
            cache_queue.remove(city)
            cache_queue.append(city)
            result += 1
        # miss
        else:
            # full
            if cache_queue and len(cache_queue) == cacheSize:
                cache_queue.popleft()
                cache_queue.append(city)
            else:
                cache_queue.append(city)
            result += 5
    for city in cities:
        cache(city)
    #print(result)
    return result
    
                
        
        
        
    
        