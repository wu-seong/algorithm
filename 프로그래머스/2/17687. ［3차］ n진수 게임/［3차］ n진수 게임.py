def transfer(num, n):
    t = ["A","B","C","D","E","F"]
    result = []
    while num >= n:
        result.append(num%n)
        num = num // n
    result.append(num)
    result = list(reversed(result))
    if n <= 10:
        return result
    t_result = []
    for n in result:
        if n < 10:
            t_result.append(n)
        else:
            t_result.append(t[n%10])
    return t_result
    
def solution(n, t, m, p):
    # 시뮬레이션 돌리면서 구하기 1000 * 100 = 100,000 * logn
    # 리스트 만들기 
    result = []
    # n진수로 변환하기
    # 나머지 연산하고 몫 연산하면서 몫이 n보다 작을 때 까지
    # 나머지가 두 자릿수 이상인 경우에는
    i = 0
    num = 0
    while i < (t-1)*m + p:
        temp = transfer(num, n)
        result.extend(temp)
        #print(temp)
        num += 1
        i += len(temp)
    answer = []
    #print(result)
    for i in range(len(result)):
        if i%m == p-1:
            answer.append(result[i])
        if len(answer) == t:
            break
    #print("".join(map(str,answer)))
    return "".join(map(str,answer))
    #return "".join(answer)
    # 10 -> A ~ 15 -> F로 변환
    # 리스트에 추가하기 
    # 추가할 때 마다 카운팅 하면서
    # 카운팅이 (t-1)* m + p-1 인덱스 까지 구하기
    