import sys
input = sys.stdin.readline
print = sys.stdout.write

N, X = map(int, input().rstrip().split(" "))

count_of_visitor = list(map(int, input().rstrip().split(" ")))
# start = 0, end = x-1 로 시작해서 누적합을 구한 뒤 sum - start, start += 1 sum + end, end +=1, end == N 일 때까지 
# 누적합 구할 때 마다 max와 비교 크면 갱신 count =1, 같으면 count+1 작으면 넘어감

acc_sum = 0
for i in range(0, X):
    acc_sum += count_of_visitor[i]

max = acc_sum
start = 0
end = X
count = 1
while end < N:
    acc_sum -= count_of_visitor[start]
    acc_sum += count_of_visitor[end]
    if max < acc_sum:
        max = acc_sum
        count = 1
    elif max == acc_sum:
        count += 1
    start += 1
    end += 1
if max == 0:
    print("%s\n" % "SAD")
    exit()
print("%s\n" % max)
print("%d\n" % count)
