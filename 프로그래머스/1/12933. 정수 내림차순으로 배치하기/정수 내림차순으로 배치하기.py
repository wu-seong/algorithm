def solution(n):
    # iteratable하게 만들기
    n_array = list(map(int, str(n)))
    # 내림차순 정렬
    n_array.sort(reverse=True)
    # 다시 하나의 정수로 합치기
    result = 0
    scale = 1
    for i in range(len(n_array)-1, -1, -1):
        result += scale*n_array[i]
        scale *= 10
    return result