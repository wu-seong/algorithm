def solution(l,r):
    # 각 수당 약수의 개수 구하기
    sum = 0
    for i in range(l,r+1):
        # 각 수 제곱근까지 나누어 떨어지는지를 확인
        cnt = 0
        for j in range(1, int(i**(0.5) ) + 1 ):
            if i % j == 0:
                if i / j == j: # 제곱근일 경우
                    cnt += 1
                else:
                    cnt += 2
        #print(cnt)
        if cnt % 2 == 0:
            sum += i
        else:
            sum -= i
    #print(sum)
    return sum