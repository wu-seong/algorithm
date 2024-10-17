def is_prime(num):
    # 제곱근 이하의 정수로 나눴는데 나누어 1이외에 나누어 떨어지는 것이 있으면 소수가 아님
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def solution(nums):
    # 완탐 - 50c3 * log 1000 충분
    cnt = 0
    n = len(nums)
    for x in range(n):
        for y in range(x+1, n):
            for z in range(y+1, n):
                if is_prime(nums[x] + nums[y] + nums[z]):
                    cnt += 1
    #print(cnt)
    return cnt
    
    