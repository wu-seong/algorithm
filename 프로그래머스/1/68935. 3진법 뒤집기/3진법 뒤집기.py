def solution(num):
    result = 0
    third_digit = ""
    while num >= 3:
        third_digit = str(num % 3) + third_digit
        num = num//3
    third_digit = str(num) + third_digit
    #print(third_digit)
    for index, digit in enumerate(third_digit):
        result += int(digit) * (3**index)
    return result