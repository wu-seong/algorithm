def solution(n, arr1, arr2):
    # arr1,2 각각 이진 문자열로 바꾸기
    # and연산하기
    # 1인 부분 # 0은 공백으로 출력하기
    result = []
    for num1, num2  in zip(arr1,arr2):
        num1 = (bin(num1))[2:]
        num2 = (bin(num2))[2:]
        num1 = ('0'*(n-len(num1))) + num1
        num2 = ('0'*(n-len(num2))) + num2
        #print(num1,num2)
        temp = ['#' if int(num1[i]) or int(num2[i]) else ' ' for i in range(n)]
        result.append("".join(temp))
    #print(result)
    return result