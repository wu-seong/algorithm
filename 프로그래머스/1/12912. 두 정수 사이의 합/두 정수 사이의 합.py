#https://school.programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    # 만약 a == b 라면 둘 중 하나를 리턴
    if a == b:
        return a
    # 그렇지 않다면 시그마 연산 하여 각 누적합 구하기
    bigger = a if a > b else b
    smaller = a if a < b else b
    # sum(1~bigger) - sum(1~(smaller-1))
    if smaller < 0:
        smaller_sum = -(smaller*(smaller-1))/2
        if bigger < 0: 
            bigger_sum = -(bigger*(bigger-1))/2
            return smaller_sum - bigger_sum + bigger
        else:
            bigger_sum = (bigger*(bigger+1))/2
            return bigger_sum + smaller_sum
    else:
        bigger_sum = (bigger*(bigger+1))/2
        smaller_sum = (smaller*(smaller+1))/2
        return bigger_sum - smaller_sum + smaller 