def solution(arr):
    # 배열을 순회하면서 앞과 다른 수이면 새로운 배열에 추가
    new_arr = []
    previous = -1
    for num in arr:
        if num != previous:
            new_arr.append(num)
            previous = num
    #print(new_arr)
    return new_arr
        