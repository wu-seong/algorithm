N,S = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))


min = N+1
sum = 0
start = 0
i = -1
while(True):
    # 끝에 도달하거나 최소 길이인 1이면 그만
    if i == N or min == 1:
        break

    if sum >= S:
        length = i - start +1
        # print("sum: ",sum)
        # print(length)
        # 길이가 더 짧으면 최솟값 갱신
        if length < min:
            min = length
        sum -= nums[start]
        start += 1
    else:
        i += 1
        if i == N:
            break
        sum += nums[i]
if min == N+1:
    min = 0
print(min)