def solution(arr, divisor):
    # arr를 순회하며 divisor로 나누어 떨어지는지를 판단하여 리스트에 넣기
    # result = []
    # for num in arr:
    #     if num % divisor == 0:
    #         result.append(num)
    # 리스트 조건식 이용하기
    result = [x for x in arr if x % divisor == 0]
    # 리스트 오름차순 정렬
    result.sort()
    # 리스트가 비었다면 -1담아 리턴
    if not result:
        result.append(-1)
    return result
