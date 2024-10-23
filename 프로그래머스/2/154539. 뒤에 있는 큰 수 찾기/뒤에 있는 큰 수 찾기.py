def solution(numbers):
    # 앞에거보다 더 큰게 오면 그게 앞에것의 뒷큰 수
    # 그 앞에것보다 작거나 같을 때 까지 뒷큰 수임
    # 해당 인덱스에 뒷큰 수 저장
    n = len(numbers)
    stack = []
    # 작거나 같은게 오면 저장하기 (값, 인덱스)
    # numbers 길이 만큼 진행
    result = [-1] * n
    for i in range(n):
        num = numbers[i]
        if stack and num > stack[-1][0]: # stack이 안비었고 더 큰 값이 올 때
            while stack and num > stack[-1][0]:
                number, idx = stack.pop()
                result[idx] = num
        stack.append((num,i))
    #print(result)
    return result
    