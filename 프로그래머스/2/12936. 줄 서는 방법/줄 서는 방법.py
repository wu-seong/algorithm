def solution(n, k):
    '''
    순열 구하기 -> x
    모든 순열을 구하는 건 오래 걸림
    
    사전 순으로 정렬했을 때 k번째의 규칙을 찾기
    
    k-1을 n-1!으로 나눈 몫을 구한다.
    해당 몫에
    몫을 인덱스로 하여 해당하는 숫자를 추가하고 지운다.
    1 2 3 4
    4 -> 인덱스 0  5 -> 인덱스 0
    1 추가 및 삭제 
    2 3 4           
    4 -> 인덱스 2  5 -> 인덱스 1
    4 추가 및 삭제
    2 3
    0 -> 인덱스 0
    2 추가 및 삭제
    3
    한개만 남으면 그냥 추가
    
    k-1을 n-1!의 나머지로 만든다 (0 <= k < n-1!)
    그것을 n-2!으로 나눈 몫을 구한다 -> 2
    
    1 2 3 4
    1 2 4 3
    1 3 2 4
    1 3 4 2
    1 4 2 3 <--
    1 4 3 2
    
    2 1 3 4
    2 1 4 3
    2 3 1 4
    2 3 4 1
    2 4 1 3
    2 4 3 1
    ...
    4 3 2 1
    '''
    
    '''
    k-1 n-1!으로 나누기
    '''
    factorial = [0] * (n+1)
    factorial[0] = 1
    for i in range(1, n+1):
        factorial[i] = i * factorial[i-1]
    #print(factorial)
    
    num_list = [i+1 for i in range(n)]
    #print(num_list)
    k = k-1
    i = n-1
    result = []
    while num_list:
        quo = k // factorial[i]
        result.append(num_list[quo])
        del num_list[quo]
        k = k % factorial[i]
        i -= 1
    #print(result)
    return result
        