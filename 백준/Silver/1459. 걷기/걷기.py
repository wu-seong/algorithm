x,y,w,s = map(int,input().split())

short = min(x,y)
long = max(x,y)
diagonal_cost = min(2*w,s) # 대각선 최소 비용
double_cost = min(w,s) # x,y 이동 최소 비용

rest = (long - short) % 2
#print(rest)
# 대각선으로 먼저 짧은 곳 도착, 이후 1차원 이동(홀수면 한칸은 바로 이동)
total_cost = (short * diagonal_cost) + ( ( (long-short-rest) * double_cost) + (rest*w))
print(total_cost)


    