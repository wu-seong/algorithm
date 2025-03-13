'''
이진수로 변환해서 배열로 나타내기
-> bin 함수로 이진수로 바꾸고 n - 길이 만큼 앞에 0 붙이기


두 배열 or연산해서 최종 문자열 만들기
'''
def solution(n, arr1, arr2):
    def to_str(num): # 숫자 받아서 0,1로 이루어진 문자열로 바꾸기
        bin_num = bin(num)[2:]
        need_zero = n - len(bin_num)
        return '0'*(need_zero) + bin_num
    # 숫자 모두 문자열로 바꾸기
    for i, n1 in enumerate(arr1):
        arr1[i] = to_str(n1)
    for i, n2 in enumerate(arr2):
        arr2[i] = to_str(n2)
    # for a in arr1:
    #     print(a)
    result = []
    for i in range(n):
        temp = []
        for j in range(n):
            # 배열을 먼저 만들기
            # 둘 중 하나라도 '1'이면 #
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                temp.append('#')
            else:
                temp.append(' ')
            # 문자열로 변환
        #print(temp)
        temp = ''.join(temp)
        result.append(temp)
    return result

   