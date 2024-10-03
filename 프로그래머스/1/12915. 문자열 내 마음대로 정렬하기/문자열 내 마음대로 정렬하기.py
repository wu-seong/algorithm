def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))
    #print(strings)
    return strings