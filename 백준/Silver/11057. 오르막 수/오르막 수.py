import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

acc_sum = [1]*10
for i in range(N):
    for j in range(1,10):
        acc_sum[j] += acc_sum[j-1]
        #print("%d\n"%acc_sum[j])    
print("%d\n"%(acc_sum[9]%10007))