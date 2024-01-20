import sys
print = sys.stdout.write
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    nums = list(map(int, input().rstrip().split(" ")))
    accSum = 0
    accSums = [0 for __ in range(N)]
    for i in range(N):
        accSum += nums[i]
        accSums[i] = accSum
    max = accSums[0]
    # print("%s\n" % accSums)
    for i in range(N-1):
        for j in range(i+1,N):
            # 빼는거면 걍 그대로
            if accSums[i] > 0:
                subarraySum = accSums[j]
            else:
                subarraySum = accSums[j]-accSums[i]
            if subarraySum > max:
                max = subarraySum
    print("%s\n" % max)

