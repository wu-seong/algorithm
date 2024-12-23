'''
각 1개씩 먼저 dp구하기
그다음 2개짜리 dp구하기
2개짜리는 만약 start와 end가 같으면 start 값에 1을 더함
3개이상은 만약 start와 end가 같으면 start+1, end -1이 True인지를 구하기
True일 때 마다 최댓값 갱신
...
n개짜리 dp구하기
'''

def solution(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    #print(dp)
    # 11 22 33 44
    # 12 23 34 45
    result = 1
    for length in range(1,n):
        for start in range(n):
            #print(start, start+length, result)
            if start+length == n:
                break
            if length == 1:
                if s[start+length] == s[start]:
                    dp[start][start+length] = True
                    result = max(result, 2)
            else:
                if s[start+length] == s[start]:
                    if dp[start+1][start+length-1]:
                        dp[start][start+length] = True
                        result = max(result, length+1)
    print(result)
    return result
        
        
        
        