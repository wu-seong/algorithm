def solution(s):
    cnt = 0
    for c in s:
        if c == 'y' or c =='Y':
            cnt += 1
        if c == 'p' or c =='P':
            cnt -= 1
        #print(cnt)
    return True if not cnt else False