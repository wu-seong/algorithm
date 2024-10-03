def solution(n, arr1, arr2):
    # arr1,2 각각 이진 문자열로 바꾸기 -> 비트 연산자 이용하면 안바꾸고도 or 연산 가능
    # or연산하기 -> 각각을 or연산보다 '|' 비트 연산자 활용 가능
    # 1인 부분 # 0은 공백으로 출력하기
    result = []
    for num1, num2  in zip(arr1,arr2):
        #print(num1,num2)
        or_bit_str = bin(num1|num2)[2:]
        or_bit_str = ('0'*(n-len(or_bit_str))) + or_bit_str
        or_bit_str = or_bit_str.replace('1', '#')
        or_bit_str = or_bit_str.replace('0', ' ')
        #print(or_bit_str)
        result.append(or_bit_str)
    #print(result)
    return result