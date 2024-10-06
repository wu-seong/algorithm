from collections import defaultdict
def solution(name, yearning, photos):
    # 사진마다 추억 점수가 있다.
    # 사진의 추억 점수는 각 인물이 가지는 그리움 점수의 총 합
    # 각 인물을 key로 하여 그리움 점수를 value로 하기 없으면 0점 -> defaultdict
    # 각 사진을 순회 하며 각 인물의 점수를 모두 합산하여 저장하기
    
    # dict 정보 만들기
    dict = defaultdict(int)
    for n,y in zip(name,yearning):
        dict[n] = y
    #print(dict)
    
    # 순회하면서 합산하고 result에 저장하기
    result = []
    for photo in photos:
        sum = 0
        for n in photo:
            sum += dict[n]
        result.append(sum)
    #print(result)
    return result
    