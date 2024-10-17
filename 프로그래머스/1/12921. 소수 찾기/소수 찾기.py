def is_prime(p_list, num):
    for p in p_list:
        if p > num**0.5:
            break
        if num % p == 0:
            return False
    return True
def solution(n):
    # 소수 리스트 만들기
    # 소수 리스트 중 제곱근 이하인 것으로 안나누어 떨어지면 소수
    # 1개라도 나누어 떨어지면 소수가 아님
    p_list = []
    for i in range(2,n+1):
        if is_prime(p_list, i):
            p_list.append(i)
    #print(p_list)
    return len(p_list)
            
            