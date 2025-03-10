'''
0을 제외한 숫자가 번호에 있는지 확인하고 카운팅
순위: 7 - 맞춘 개수, 맞춘 개수 1이하이면 -> 6

최고순위는 0의 개수를 맞춘 개수에 더하기
'''
def solution(lottos, win_nums):
    # 순회하면서 당첨 숫자 여부 확인
    cnt = 0
    zero = 0
    for l in lottos:
        if l == 0:
            zero += 1
        if l in win_nums:
            cnt += 1
    print(cnt, zero)
    # 0 카운팅
    # 최악은 그냥 당첨 숫자로만 랭크 확인
    if cnt <= 1:
        bad = 6
    else:
        bad = 7 - cnt
    
    cnt += zero
    if cnt <= 1:
        good = 6
    else:
        good = 7 - cnt
    return [good, bad]
        
   