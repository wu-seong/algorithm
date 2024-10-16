def solution(k, m, score):
    # 가장 낮은 점수를 기준으로 가격이 결정
    # 남는 사과는 버린다.
    # 크기 순으로 정렬한 뒤에 m의 나머지는 버림
    # 이익이 발생하지 않는 경우는 0
    
    # 크기 순 정렬 및 슬라이싱으로 나머지 버리기
    score.sort(reverse=True)
    score = score[:len(score)-(len(score)%m)]
    #print(score)
    # 박스마다 점수 계산해서 더하기
    # 높은것 먼저
    result = 0
    for i in range(0,len(score),m):
        box = score[i:i+m]
        result += min(box)*m
    #print(result)
    return result