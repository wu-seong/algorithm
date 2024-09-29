def search_divied_num(num):
    result = []
    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            result.append(i)
            result.append(num//i)
    return set(result)

def search_multiple_num(num, max_range):
    result = []
    origin_num = num
    while num <= max_range:
        result.append(num)
        num += origin_num
    return set(result)
def solution(n, m):
    # 최대 공약수 찾기
    # 각 수의 공약수 찾기 -> 같은 것 모두 찾기 -> 최댓값 찾기
    n_d_list = search_divied_num(n)
    m_d_list = search_divied_num(m)
    max_d = max(n_d_list & m_d_list)
    # 최소 공배수 찾기
    # 두 수를 곱하여 공배수 범위 찾기
    # 범위까지 각 수의 배수를 구하고 최솟값을 찾기
    n_m_list = search_multiple_num(n, n*m)
    m_m_list = search_multiple_num(m, n*m)
    min_m = min(n_m_list & m_m_list)
    # 배열 만들어 반환하기
    #print(max_d,min_m)
    return [max_d, min_m]