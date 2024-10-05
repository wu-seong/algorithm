from collections import deque
def get_d_nums(num):
    result = set([])
    for i in range(1, int(num**(0.5))+1):
        if num % i == 0:
            result.add(i)
            result.add(num//i)
    return result
def get_m_num(num1, num2):
    d_num1 = get_d_nums(num1)
    d_num2 = get_d_nums(num2)
    return num1*num2/(max(d_num1&d_num2))
def solution(arr):
    arr = deque(list(set(arr)))
    # 두 수를 비교해서 최소 공배수 구하기
    # 해당 수와 다른 수를 다시 비교하기
    # 
    while len(arr) != 1:
        new_num = get_m_num(arr.popleft(), arr.popleft())
        arr.append(new_num)
    #print(arr)
    return arr[0]
        