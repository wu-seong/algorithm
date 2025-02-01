'''
N글자 끼리 분류후에
각 글자 마다 성적 순으로 분류?

만약 모두 같은 글자라면?
1: 
2: 12
3: 32 31
4: 43 42

같은 글자이고 등수가 1씩 차이 날 때 점화식 = ((N-K) * K) + (K * (K-1))/2


현재 등수 - K의 범위의 개수를 알아야 한다.

현재 등수, 등수+K 까지 imos 체크해놓고 스위핑하기?

1 1 1 0 -1 -1 -1
1 2 3 3 2 1 0

'''
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())



sums = [[0 for _ in range(N+1)] for _ in range(21)]
len_list = [0]
for i in range(1,N+1):
    name = input().rstrip()
    len_list.append(len(name))
    if i+1 <= N:
        sums[len(name)][i+1] += 1
    end = i + K + 1
    if end <= N:
        sums[len(name)][end] -= 1

for i in range(2, 21):
    for j in range(2, N+1):
        sums[i][j] += sums[i][j-1]
#print(sums)

result = 0
for i in range(1, N+1):
    result += sums[len_list[i]][i]
print(result)