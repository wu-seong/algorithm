def solution(x):
    # x가 각 자리수의 합으로 나누어 떨어지는 지를 판별
    # 각 자리수의 합 구하기
    sum = 0
    for digit in list(map(int, str(x))):
        sum += digit
    # 합으로 나누어 떨어지는 지 여부를 판단하기
    return (x % sum) == 0