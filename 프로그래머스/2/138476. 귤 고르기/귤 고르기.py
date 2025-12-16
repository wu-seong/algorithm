'''
종류를 최대한 적게 유지
갯수가 많은 종류를 우선으로 선택

각 종류마다 개수를 알아야함
개수를 구한 뒤에
개수가 많은 순으로 정렬?

카운팅한 뒤에는 
key는 중요하지 않고 value만 구하면 되긴함
value만 구해서 리스트에 넣고 정렬
개수가 많은 순서대로 value값을 k에서 빼기
k = k - value
카운팅 
k > 0 계속 
k <= 0 끝
'''
from collections import defaultdict

def solution(k, tangerine):
    # 카운팅
    c_dict = defaultdict(int)
    for v in tangerine:
        c_dict[v] += 1
    #print(c_dict)
    # value 기준으로 key 정렬
    sorted_value = sorted(c_dict.values(), reverse=True)
    #print(sorted_value)
    
    # 바구니에 담기
    result = 0
    for v in sorted_value:
        k -= v
        result += 1
        if k <= 0:
            return result
    return result

'''
tc1) k=1, [1] -> 1
tc2) k=2, [2,2] -> 1
tc3) k=2, [1,2] -> 2
'''