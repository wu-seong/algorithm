import itertools
def solution(numbers):
    # 세 정수의 합이 0이면 삼총사
    # 조합
    comb = itertools.combinations(numbers, 3)
    cnt = 0
    for x,y,z in list(comb):
        if x+y+z == 0:
            cnt += 1
    #print(cnt)
    return cnt