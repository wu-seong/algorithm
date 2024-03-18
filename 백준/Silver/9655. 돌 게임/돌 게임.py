import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

winner = [0 for _ in range(N)]
# 상근이 먼저 시작 상근 = sk, 창영 = cy , 1 or 3
winner[0] = "SK"

if(N == 1):
    print("SK\n")
    exit()
winner[1] = "CY"
for i in range(2,N):
    winner[i] = winner[i-2]
print("%s\n"%winner[N-1])
