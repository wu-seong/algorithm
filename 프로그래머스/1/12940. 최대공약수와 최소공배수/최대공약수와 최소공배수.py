def search_divied_num(num):
    result = []
    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            result.append(i)
            result.append(num//i)
    return set(result)
def solution(n, m):
    # 최대 공약수 찾기
    # 각 수의 공약수 찾기 -> 같은 것 모두 찾기 -> 최댓값 찾기
    n_d_list = search_divied_num(n)
    m_d_list = search_divied_num(m)
    max_d = max(n_d_list & m_d_list)
    #print(max_d,min_m)
    return [max_d, n*m/max_d]