def gcd(a,b):
    if a < b:
        b, a = a, b
    #print(a,b)
    if a % b == 0:
        return b
    else:
        r = a % b
        a = b
        b = r
    return gcd(a,b)
def solution(arrayA, arrayB):
    """
    철수가 가진 카드의 공약수 구하기 1~N
    영희가 가진 카드의 공약수 구하기 1~M
    
    1. arrayA 최대공약수 구하기 
    2. arrayB 최대공약수 수하기
    3. A의 최대 공약수로 
    최대 공약수 a가 b가 서로소가 아니면 0임
    """
    result_a, result_b = arrayA[0], arrayB[0]
    for v in arrayA:
        result_a = gcd(result_a, v)
    #print(result_a)
    for v in arrayB:
        result_b = gcd(result_b, v)
    #print(result_b)
    
    # 직접 구한 공약수로 나눠보기
    if result_b == 1 and result_a == 1:
        return 0
    result = 0
    if result_a != 1:
        for v in arrayB:
            if v % result_a == 0:
                break
        else:
            result = result_a
    if result_b != 1:
        for v in arrayA:
            if v % result_b == 0:
                return result
        else:
            if result_b > result_a:
                result = result_b
    return result
    #print(gcd(arrayA[0], arrayA[1]))