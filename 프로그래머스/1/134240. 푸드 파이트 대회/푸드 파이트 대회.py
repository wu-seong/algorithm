def solution(food):
    left = ""
    for i in range(1,len(food)):
        left += str(i)*(food[i]//2)
    # 2로 나눈 몫 만큼 인덱스 문자열 추가            
    #print(left)
    # origin + 0 + reversed
    return left + '0' + left[::-1]