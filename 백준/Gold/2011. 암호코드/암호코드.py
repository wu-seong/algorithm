import sys
input = sys.stdin.readline

'''
글자 수를 하나씩 늘려가면서 해당 글자 마다 나올 수 있는 경우의 수를 구하기

처음에는 1자리로
나올 수 있는 경우: 1~9 -> 그대로 매칭 
두자리인 경우 = 본래 암호가 두자리 짜리인경우 + 1자리 + 1자리인 경우
세자리인 경우 = 본래 암호가 1 + 2인 경우, 2 + 1인경우 1 + 1+ 1인 경우


25114
2 -> 2로 해석
n을 더하는 경우의 수를 구하기

한 자리를 추가하면 현재 자리를 그냥 추가하는 경우(dp[i-1]) + 이전과 결합해서 보는 경우(dp[i-2])
이전과 결합을 하기 위한 조건이 있음 이전과 합친 것이 10~26 사이어야 합치는 것이 가능


25114일 때 
2 -> 1
25 -> 1 + 1 = 2
251 -> 2 + 0= 2
2511 -> 2 + 2 = 4
25114 -> 4 + 2 = 6 

독립되서 쓰기 -> dp[i-1] (0아닌지 체크 필요)
결합해서 쓰기 -> dp[i-2] (결합 가능 체크 필요)

암호가 잘못된 경우: 이전에 3 이상이 나왔는데 0이 나오거나 0이 나왔는데 또 0이 나온 경우
'''
def solution(num):
  n = len(num)
  def is_alpha(num_str):
    if 10 <= int(num_str) <= 26:
      return True
    return False
  dp = [0] * (n+1) 
  dp[0] = 1

  # 0이 경우
  if num[0] == '0':
    print(0)
    return 
  if n >= 2:
    if is_alpha(num[:2]):
      dp[1] += 1
    if num[1] != '0':
      dp[1] += dp[0]
    else:
      if not is_alpha(num[:2]):
        print(0)
        return 
    
  for i in range(2, n):
    # 알파벳 결합 확인
    if is_alpha(num[i-1:i+1]):
      dp[i] += dp[i-2]
    # 0확인
    if num[i] != '0':
      dp[i] += dp[i-1]
    # 0이면 올바른지도 확인, 0인데 앞이랑 결합을 못하면 안됨
    else:
      if not is_alpha(num[i-1:i+1]):
        print(0)
        return
    dp[i] %= 1000000
  #print(dp)
  print(dp[n-1])



solution(input().rstrip())