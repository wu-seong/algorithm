import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
nums = list(map(int, input().split(" ")))
M = int(input())
accSums = [0 for _ in range(M)]

accSum = 0
for a in range(N):
    accSum += nums[a]
    accSums[a] = accSum
# print(accSums)   
for b in range(M):
    i,j = map(int, input().rstrip().split(" "))
    if i == 1:
        print("%s\n" % accSums[j-1])
    else:
        value = accSums[j-1]-accSums[i-2]
        print("%s\n" % value)
