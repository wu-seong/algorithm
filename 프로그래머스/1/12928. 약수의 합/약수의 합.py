def solution(n):
    if n == 1:
        return 1
    sum = 0
    check = [False] * (n+1)
    for i in range(1, (n//2)+1):
        if not check[i] and n/i == n//i: # 이전에 약수로 구해지지 않았고, 어떤 수로 나누어 떨어진다면
            if i == n/i: # 제곱근일때
                check[i] = True    
                sum += i 
                continue
            check[i] = True
            check[int(n/i)] = True
            sum += i + n/i
    return sum
