'''
n자리 수에서 오름차순으로 이루어진 경우의 수를 모두 구하기
1자리 수
0~9 -> 10
2자리 수

다음에 0으로 시작할 수 있는 건 0으로 끝난 것 개수
1로 시작할 수 있는 건 0,1 개수
2로 시작할 수 있는 건 0,1,2 개수

9로 시작할 수 있는 건 0,1,2 ... 9 개수

각 자릿수 마다 n으로 끝난 것의 개수를 카운팅
다음 개수를 구할 때는 이전에 카운팅 한 것을 자릿수마다 적절히 더해서 구하기
0 -> 0
1 -> 0,1
'''
import sys
input = sys.stdin.readline
cnt = [[0 for _ in range(10)] for _ in range(65)] # n 자릿수에서 0 ~ 9 로 끝나는 것 카운팅
for i in range(10):
    cnt[1][i] = 1
sums = [0 for _ in range(65)]
sums[1] = 10
for i in range(2,65):
    for j in range(10):
        for k in range(j+1):
            cnt[i][j] += cnt[i-1][k]
    sums[i] = sum(cnt[i])
#print(sums)
T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    print(sums[n])
    