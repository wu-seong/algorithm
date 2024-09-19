def is_prime(num):
    if num == 1:
        return False
    root = int(num**(1/2)//1)
        #print(num, root)
    for n in range(2,root+1):
        if num % n == 0:
            return False
    return True
def solution(n, k):
    t_n = ""
    while n > 0:
        rest = n % k
        n = n//k
        t_n = str(rest) + t_n
    #print(t_n)
    cnt = 0
    temp = ""
    for num in t_n:
        if num == '0': # 0이면 그전 숫자 소수 판별
            if temp != "" and is_prime(int(temp)):
                cnt += 1
            temp = ""
        else:
            temp = temp + num
    if temp != "" and is_prime(int(temp)): #마지막 숫자 소수 판별
        cnt += 1
        #print(cnt)
    return cnt
solution(110011, 10)