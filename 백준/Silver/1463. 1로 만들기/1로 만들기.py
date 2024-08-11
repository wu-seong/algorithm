N = int(input())
nums = [0 for i in range(N+1)]

for i in range(2,N+1):
    # 이전 solve 참고해서 최솟값 구하기 
    minus = nums[i-1]
    m = minus
    if i % 3 == 0:
        three = nums[i//3]
        m = min(m, three)
    if i % 2 == 0:
        two = nums[i//2]
        m = min(m, two)
    nums[i] = m + 1
print(nums[N])
    
