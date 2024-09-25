def solution(n):
    # n이 어떤 양수 정수의 제곱이라면 제곱근을 구했을 때, 정수일 것이다.
    # 루트 n이 정수인지를 판단
    # 정수 판단 방법 -> 1으로 나눈 몫이 원래와 같다면(소수 점이 존재한지 않는다면) 정수임
    root = n**(1/2)
    print(root)
    if root.is_integer():
        return (root+1)**2
    else:
        return -1