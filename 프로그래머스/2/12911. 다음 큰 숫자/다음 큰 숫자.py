def to_binary_cnt(n):
    result = ""
    while n >= 2:
        result += str(n%2)
        n = n//2
    result += str(n)
    result = result[::-1]
    cnt = result.count('1')
    #print(cnt)
    return cnt
def solution(n):
    # 현재 숫자의 1의 개수를 세기
    target_cnt = to_binary_cnt(n)
    # 숫자를 1 늘리고 2진수로 변환해서 1의 개수가 같다면 해당 십진수 반환
    while True:
        n = n+1
        cnt = to_binary_cnt(n)
        if cnt == target_cnt:
            return n