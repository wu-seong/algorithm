import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
num = list(map(int ,input().rstrip().split(" ")))

acc_sum = 0
sum_list = [0 for _ in range(N)]
# 누적합 구하고
for i in range(N):
    acc_sum += num[i]
    sum_list[i] = acc_sum
# 누적합(i-1) * 수 (i), n = 1 to n까지 
result = 0
for i in range(1,N):
    result += num[i]*sum_list[i-1]
print("%d\n"%result)
