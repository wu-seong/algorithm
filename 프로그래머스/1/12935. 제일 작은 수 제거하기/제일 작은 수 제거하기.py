def solution(arr):
    # 가장 작은 원소 찾기
    min_num = arr[0]
    for i in range(1,len(arr)):
        min_num = min(min_num, arr[i])
    # 제거
    arr.remove(min_num)
    # 비어있으면 [-1] 리턴
    return arr if arr else [-1]