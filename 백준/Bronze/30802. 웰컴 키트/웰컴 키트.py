'''
23
3 1 4 1 5 9
5 7


'''
import sys
input = sys.stdin.readline
N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

T, P = map(int, input().rstrip().split())

t_cnt = 0

for num in nums:
    t_cnt += num //T
    if num % T:
        t_cnt += 1
        
p_cnt = N // P
ps_cnt = N % P
print(t_cnt)
print(p_cnt, ps_cnt)
    