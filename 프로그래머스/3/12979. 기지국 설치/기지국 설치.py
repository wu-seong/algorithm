'''
N개에서 1+2W 만큼을 빼는 것이 일반적, 하지만 겹치는 부분과 끝 부분이 생긴다.

일단 첫 station의 왼쪽 도달거리 구하기
도달하지 못하는 거리 만큼은 (거리-1)//(2W+1) + 1로 구하기, 거리 == 0이면 0 
6 0 - 0 1~5 -> 1 6~10 -2

현재 station과 다음 station의 거리차가 2w이하이면 계속 next로 넘어가기
간격 // (2w + 1)   한것만큼 더하기

마지막 station도 오른쪽 간격이 0 = 0 1~2w+1 -> 1
(거리-1) // (2W+1) + 1

'''
def solution(N, stations, W):
    result = 0
    s_distance = (stations[0] - W) - 1
    if s_distance > 0:
        result += ((s_distance - 1) // ((2*W) + 1)) + 1
    e_distance = (N - (stations[-1] + W))
    if e_distance > 0:
        result += ((e_distance - 1) // ((2*W) + 1)) + 1
    for i, s in enumerate(stations[:-1]):
        d = stations[i+1] - s - 1
        if d <= 2*W:
            continue
        result += d // ((2*W) + 1)
        
    print(result)
    return result

        