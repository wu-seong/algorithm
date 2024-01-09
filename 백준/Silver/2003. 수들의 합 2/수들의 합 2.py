N,M = map( int, input().split(" "))
nums = list(map(int, input().split(" ")))
# print(nums)

count = 0
sum = 0
start = 0
i = -1
while(True):
    if sum == M:
        count += 1
        sum -= nums[start]
       # print(sum)
        start += 1
    elif sum > M:
        sum -= nums[start]
       # print(sum)
        start += 1
    else:
        i += 1
        if i == N:
            break
        sum += nums[i]
       # print(sum)
print(count)
    
