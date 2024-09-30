def solution(A,B):
    # A 오름차순 정렬,B 내림차순 정렬
    A.sort()
    B.sort(reverse=True)
    sum = 0
    for a,b in zip(A,B):
        sum += a*b
    print(sum)
    return sum