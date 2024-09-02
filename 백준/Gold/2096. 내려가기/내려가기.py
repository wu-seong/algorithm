import sys
input = sys.stdin.readline

N = int(input().rstrip())
small_dp = [0 for _ in range(3)]
large_dp = [0 for _ in range(3)]
# 첫번째는 dp는 숫자 그대로
small_dp = list(map(int, input().rstrip().split()))
large_dp = small_dp[::]
# 두번째 부터는 맨 왼쪽은 이전의 0,1 중 큰 것
# 중간은 0,1,2 중
# 오른쪽은 1,2 중 큰 것
large_tmp = large_dp[::]
small_tmp = small_dp[::]
for i in range(1,N):
    large_tmp = large_dp[::]
    game = list(map(int, input().rstrip().split()))
    large_dp[0] = game[0] + max(large_tmp[0], large_tmp[1])
    large_dp[1] = game[1] + max(large_tmp[0], large_tmp[1], large_tmp[2])
    large_dp[2] = game[2] + max(large_tmp[1], large_tmp[2])

    small_tmp = small_dp[::]
    small_dp[0] = game[0] + min(small_tmp[0], small_tmp[1])
    small_dp[1] = game[1] + min(small_tmp[0], small_tmp[1], small_tmp[2])
    small_dp[2] = game[2] + min(small_tmp[1], small_tmp[2])
print(max(large_dp), min(small_dp))