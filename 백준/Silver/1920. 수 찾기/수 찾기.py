import sys
input = sys.stdin.readline

N = int(input())
nums = set(map(int, input().rstrip().split()))

M = int(input())
find_nums = list(map(int, input().rstrip().split()))

for f_n in find_nums:
    if f_n in nums:
        print(1)
    else:
        print(0)