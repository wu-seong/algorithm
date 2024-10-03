def solution(food):
    # 홀수이면 -1하고
    left = ""
    for i in range(1,len(food)):
        if food[i] % 2 == 1:
            food[i] -= 1
        left += str(i)*(food[i]//2)
    # 2로 나눈 몫 만큼 인덱스 문자열 추가            
    #print(left)
    # origin + 0 + reversed
    return left + '0' + left[::-1]