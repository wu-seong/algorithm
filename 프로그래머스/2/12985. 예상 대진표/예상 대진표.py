import math
def solution(n,a,b):
    # 두 명의 차이가 1일때 까지 1을 빼고 2로 나눈 몫? + 1 
    # 두 명의 차이 1 and 다음 라운드가 같은지도 확인
    cnt = 1
    while True :
        if abs(a-b) == 1 and (a-1)//2 == (b-1)//2:
            break
        a = ((a-1)//2) + 1
        b = ((b-1)//2) + 1
        cnt += 1
    #print(cnt)
    # 4 -> 2 -> 1, 7 -> 4 -> 2 
    # 4 -> 2 -> 1 -> 1, 5 ->  -> 4 -> 2 -> 1
    return cnt