def solution(wallet, bill):
    # 더 큰 것을 반으로 나누고 정수로 만들기
    w_y, w_x = wallet
    b_y, b_x = bill
    cnt = 0
    while True:
        if (b_y <= w_y and b_x <=w_x) or (b_x <= w_y and b_y<=w_x): # 들어가면
            return cnt
        if b_y > b_x:
            b_y = b_y//2
        else:
            b_x = b_x//2
        cnt += 1
        
    
        
    # wallet에 들어갈 때 까지 (그대로 넣어보고 90도로 넣어보고 둘 다 <= 라면)