from collections import deque
def solution(cacheSize, cities):
    # 각 도시 이름을 가져오는 총 실행시간을 구하기
    # 하나의 도시를 구할 때마다 log n이어야 함
    # 처음엔 캐시가 비어있음
    # 캐시에 없는 거면 + 5 하고 캐시에 popleft + append
    # 캐시에 있는 거면 + 1 하고 delete하고 append
    # cities가 끝날 때까지
    cache = deque()
    time = 0
    for city in cities:
        city = city.lower()
        if city in cache: # 있을 때
            time += 1
            cache.remove(city)
            cache.append(city)
        else: # 없을 때
            time += 5
            if cache and len(cache) == cacheSize:
                cache.popleft()
            if len(cache) + 1 <= cacheSize:
                cache.append(city)
        #print(cache)
    #print(time)
    return time
        