def solution(num):
    # num이 1이 될 때까지 홀/짝에 맞게 작업 반복하며 작업 수 카운팅
    # 만약 cnt가 500까지 1이 되지 않는다면 -1반환
    cnt = 0
    while num != 1:
        if cnt == 500:
            return -1
        if num % 2 == 0:
            num = num/2
        else:
            num = (num*3) + 1
        cnt += 1
    return cnt