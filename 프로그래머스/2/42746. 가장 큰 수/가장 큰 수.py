from functools import cmp_to_key
def custom_compare(a,b):
    if a + b > b + a: # ab가 사전순으로 더 느린 것 a가 앞에 있어야 한다. ->a는 첫번째 즉 -1
        return -1
    elif b + a > a + b:
        return 1
    else: # 똑같은 경우 정렬하지 않는다.
        return 0 
def solution(numbers):
    if len(set(numbers)) == 1 and list(set(numbers))[0] == 0:
        return "0"
    numbers = list(map(str,numbers))
    numbers.sort(key=cmp_to_key(custom_compare))
    #print(numbers)
    # 모두 0 이면 000000이 아니라 그냥 "0임"
    return "".join(numbers)