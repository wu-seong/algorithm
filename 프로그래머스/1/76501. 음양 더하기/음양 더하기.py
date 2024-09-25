def solution(abs, signs):
    sum = 0
    for i in range(len(abs)):
        sum += abs[i] if signs[i] else -abs[i]
    return sum
        