def solution(n):
    sum = 0
    # 각 자릿수 숫자 추출해서 더하기
    for n_s in str(n):
        sum += int(n_s)
    return sum