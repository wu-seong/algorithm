from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input().rstrip())

heap = []
for _ in range(N):
    num = int(input().rstrip())
    if num:
        heappush(heap, num)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)