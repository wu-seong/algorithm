def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x: x[n])
    #print(strings)
    return strings