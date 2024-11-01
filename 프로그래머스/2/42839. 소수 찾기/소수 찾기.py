def is_prime(number):
    # number의 루트이하의 정수까지 나누어 떨어지는 수가 없으면 소수임
    if number == 1 or number == 0:
        return False
    for i in range(2, int(number**0.5) + 1):
        if (number % i) == 0:
            return False
    return True
def dfs(n, level, numbers, visited, result):
    global prime_list
    #print("level:", level,"visited: ",visited)
    if n == level: # 만약 level이 n과 같으면 소수 판별 및 카운팅
        if is_prime(int("".join(map(str,result)))):
            prime_list.add(int("".join(map(str,result))))
        return
    for i in range(len(numbers)):
        if not i in visited: # 고르지 않은 것만 고르기
            visited.add(i)
            result.append(numbers[i])
            dfs(n, level + 1, numbers, visited, result)
            result.pop()
            visited.remove(i)
    
prime_list = set()
n = 0
def solution(numbers):
    global n, prime_list
    n = len(numbers)
    # 0~9 7이하면 다해봐도 될듯? 7!임 5040 
    # dfs로 순열 구하기 
    # 각 순열 당 소수 판별하기
    # 길이가 1부터 n인 것 까지 모두 소수 찾기
    # 0으로 시작하는 건 판단할 필요가 없는듯? 013 13
    # numbers에 있는 수 리스트로 만들어서 넘기기
    numbers = list(map(int, numbers))
    
    for i in range(1,n+1):
        dfs(i, 0, numbers, set(), [])
    #print(prime_list)
    return len(prime_list)