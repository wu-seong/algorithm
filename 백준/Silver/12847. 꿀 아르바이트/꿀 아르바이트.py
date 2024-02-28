import sys
input = sys.stdin.readline
print = sys.stdout.write

n,m = map(int, input().rstrip().split(" "))
pay = list(map(int, input().rstrip().split(" ")) )

acc_pay = [0 for _ in range(n)]
sum = 0
for i in range(n):
    sum += pay[i]
    acc_pay[i] = sum
max = acc_pay[m-1]
for i in range(m, n):
    pays = acc_pay[i]-acc_pay[i-m]
    if pays > max:
        max = pays
print("%d\n"%max)