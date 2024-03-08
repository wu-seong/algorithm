import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
if n == 1:
    print("1\n")
    exit()
dynamic = [0 for _ in range(n+1)]
dynamic[1] = 1
dynamic[2] = 3
for i in range(3,n+1):
    dynamic[i] += dynamic[i-2]*2 # 2*2 인데 세로 두 줄짜리는 아래 경우와 겹침
    dynamic[i] += dynamic[i-1] # 단순히 작대기 하나 추가
print("%d\n"%(dynamic[n]%10007))