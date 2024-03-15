import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())


if N == 1:
    print("1\n")
    exit()

count = [0 for _ in range(N+1)]


count[1] = 1
count[2] = 1
for i in range(3,N+1):
    count[i] += count[i-1]
    count[i] += count[i-2]

print("%d\n"%count[N])