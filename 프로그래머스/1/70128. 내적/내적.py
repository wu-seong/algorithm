def solution(a,b):
    sum = 0
    for value_a, value_b in zip(a,b):
        sum += value_a*value_b
    return sum