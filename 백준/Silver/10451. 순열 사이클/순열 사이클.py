from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
for i in range(T):

    queue = deque()
    N = int(input())
    visited = [False] * (N+1)
    nums = list(map(int, input().rstrip().split()))
    nums.insert(0,0)

    cnt = 0
    for i in range(1,N+1):
        if visited[i]:
           continue
        index = i 
        cnt += 1
        while not visited[index] :
            visited[index] = True
            index = nums[index]
    print("%d\n" %cnt)
