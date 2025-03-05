'''
N = 1 -> 0
N = 2 -> 3
N = 3 -> 3
N = 4 -> (N-2)번째 * 3 + (N-4)번째* 2 

'''
N = int(input())
dp = [0 for _ in range(31)]
dp[0] = 0
dp[1] = 0
dp[2] = 3
dp[3] = 0
dp[4] = 11
if N % 2 == 1: # 홀수이면 0
  print(0)
  exit()


for i in range(6,31,2): # 33 + 3*11
  temp = (dp[i-2] * 3)
  for j in range(i-4,0,-2):
    temp += dp[j]*2
  temp += 2
  dp[i] += temp
#print(dp)
print(dp[N])

