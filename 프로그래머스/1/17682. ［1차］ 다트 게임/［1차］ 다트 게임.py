#def dart(scores, current):

def solution(dartResult):
    # SDT - 제곱
    # 스타상 - 이전 점수 저장, 중첩가능
    # 아차상 - 부호 예외처리, 스타와 중첩가능
    # 스타, 아차 둘 중 하나만 점수마다 가능
    
    #숫자 읽기 - 알파벳이 아닐때까지
    #제곱 읽기 - 읽어서 num 제곱하기
    #옵션 읽기 - 만약 alpha도 아니고 digit도 아니면 옵션
    sq = {'S': 1, 'D':2, 'T':3}
    n = len(dartResult)
    i = 0
    scores = []
    while i < n:
        num = 0
        while dartResult[i].isdigit():
            num = (num*10) + int(dartResult[i])
            i += 1
        
        num = num**sq[dartResult[i]]
        scores.append(num)
        i += 1
        if i < n:
            if dartResult[i] == '*': # 이전스코어와 현재 코어 두배
                scores[-1] *= 2
                if len(scores) >= 2:
                    scores[-2] *= 2
                i += 1
            elif dartResult[i] == '#': # 현재 스코어 음수
                scores[-1] *= -1
                i += 1
    #print(scores)
    return sum(scores)
    