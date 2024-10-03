def solution(brown,yellow):
    # 테두리의 둘래 = 갈색 격자의 수
    # 카펫 가로 길이 >= 세로길이
    # 꼭짓점을 뺀 둘래를 반으로 나누고 x,y를 임의로 정한다
    # x*y == 노란색인 x,y를 찾는다
    # x,y는 1이상 이어야 한다. 
    # 더큰 것을 먼저 반환
    # 반환(more+2, less+2)
    dule = int(((brown-4)/2))
    for x,y in [ (i, dule - i) for i in range(1,dule)]:
        #print(x,y)
        if x*y == yellow:
            return [max([x,y])+2, min(x,y)+2]