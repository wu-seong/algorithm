n, k = map(int, input().split())  
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]  

item = [[0, 0]]
for i in range(1, n + 1):  
    item.append(list(map(int, input().split())))

Max = 0
for i in range(1, n + 1):  
    for j in range(1, k + 1):  

        weight = item[i][0]
        value = item[i][1]
        
        if j < weight:
            dp[i][j] = dp[i - 1][j]  
            
     
        else: 
            dp[i][j] = max(dp[i - 1][j],value + dp[i - 1][j - weight])
            

print(dp[n][k])