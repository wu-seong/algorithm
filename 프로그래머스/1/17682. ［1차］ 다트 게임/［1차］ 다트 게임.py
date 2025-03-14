'''
3개의 점수를 기억하는 배열 만들기
처음에는 일단 점수와 보너스를 통해서 점수를 만든다.
그다음 옵션에 따라 수식을 만든다.
없으면 -> 그냥 + *이면 현재 점수와 이전 점수에 *2를 한다.(처음이면 현재것만)
#이면 0를 한다.

'''

def solution(dartResult):
    score = []
    option = [False] * 3
    def area(num, a):
        if a == 'S':
            return int(num)
        elif a == 'D':
            return int(num)**2
        else:
            return int(num)**3
    
    i = 0
    n = len(dartResult)
    index = -1
    while i < n:
        if dartResult[i].isdigit():
            if dartResult[i+1] == '0': # 10일때
                score.append(area('10', dartResult[i+2]))
                i += 3
                continue
            score.append(area(dartResult[i], dartResult[i+1]))
            i += 2
            index += 1
        else:
            option[index] = dartResult[i]
            i += 1
            
    #print(score)
    #print(option)
    for i in range(3):
        if option[i] == '*':
            score[i] *= 2
            if i-1 >= 0:
                score[i-1] *= 2
    result = 0
    for i in range(3):
        if option[i] == '#':
            result -= score[i]
        else:
            result += score[i]
    print(score)
    return result