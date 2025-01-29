'''
1. 입력 시간 누적 달로 게산하기
2000 1월 -> 1
(년도 - 2000) * 12
ex) 2010 04 -> 124

가장 많이 군대에 가 있는 달
= 
dp?

2023-02 2023-04
2023-03 2025-03
2023-04 2025-02
2024-02 2026-02

1 -> 95999 

각 구간 마다 모두 겹치는 인원을 세기? 1e10
누적합?

2 2 2 2 2

각 구간의 시작에 1, 끝에 -1을 더하기
누적합으로 각 구간이 몇번 나오는지를 계산
그 중에서 가장 숫자가 큰 달을 찾기, 중복이면 가장 빠른 달

범위중에서 가장 중복이 많이 되는 범위
'''

import sys
input = sys.stdin.readline

sum = [0] * int(1e5)
N = int(input().rstrip())
for _ in range(N):
    start, end = input().rstrip().split()
    s_year, s_month = map(int, start.split('-'))
    e_year, e_month = map(int, end.split('-'))
    s_acc = ((s_year-2000)*12) + s_month
    e_acc = ((e_year-2000)*12) + e_month
    #print(s_acc, e_acc)
    sum[s_acc] += 1
    sum[e_acc+1] -= 1
for i in range(1,len(sum)):
    sum[i] += sum[i-1]
max_value = 0
max_index = -1
for i in range(len(sum)):
    if sum[i] > max_value:
        max_value = sum[i]
        max_index = i
r_month = max_index%12
if r_month == 0:
    r_month = 12
if r_month < 10:
    r_month = '0' + str(r_month)
r_year = 2000 + (max_index//12)
if r_month == 12:
    r_year -= 1
print(r_year, r_month, sep='-')