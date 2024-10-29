def solution(numbers):
    # 10만 *  
    # 뒤에서 부터 해서 0이 있으면 1로 만들기 만약 모두 1이라면 앞에 1을 붙이고 그 다음을 0으로 만들기
    result = []
    for number in numbers:
        b_str = bin(number)[2:]
        #print(b_str)
        add = 1
        for digit in b_str[::-1]:
            if digit == '0':
                break
            add *= 2
        r_number = number + add - (add//2) 
        result.append(r_number)
    return result
    # 그다음 십진수 변환