from itertools import combinations
def solution(numbers):
    result = []
    comb = combinations(numbers, 2)
    for x,y in comb:
        result.append(x+y)
    result = set(result)
    result = sorted(list(result))
    #print(list(result))
    return result