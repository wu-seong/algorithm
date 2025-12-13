from collections import defaultdict 
'''
모두 합하여 다른 조합 ->

종류별 1가지 의상만 가능

최소 1개의 의상은 입는다.

서로 다른 옷의 조합의 수 =
각 종류 마다 의상의 수 + 1(안 입은 경우)를 서로 곱한다.
아예안 입은 경우(1)은 뺸다.

1. 전처리
- clothes배열의 각 원소를 받아서, key에 카운팅한다.

2. 계산
'''
def solution(clothes): 
    clothes_cnt = defaultdict(int)
    for c in clothes:
        _, key = c
        clothes_cnt[key] += 1
    #print(clothes_cnt)
    result = 1
    for key in clothes_cnt:
        #print(key)
        result *= (clothes_cnt[key] + 1)
    return result - 1

'''
tc1)
의상 수가 1개일 때 -> 1

'''