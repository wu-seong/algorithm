N,M = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))

sum = 0
count = 0
rests = []
for i in range(N):
    sum += nums[i]
    rests.append(sum%M)
    if sum % M == 0 :
        count += 1
rest_counts = [0 for i in range(M)]
for rest in rests:
    rest_counts[rest] += 1
for r_count in rest_counts:
    count += (r_count * (r_count-1))//2
print(count)

        
