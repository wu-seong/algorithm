def solution(n):
    # 현재 숫자의 1의 개수를 세기
    target_cnt = bin(n).count('1')
    # 숫자를 1 늘리고 2진수로 변환해서 1의 개수가 같다면 해당 십진수 반환
    while True:
        n = n+1
        cnt = bin(n).count('1')
        if cnt == target_cnt:
            return n