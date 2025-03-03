'''
5개의 정수 비밀번호를 맞추기

가능한 조합

30c5 = 30 29 7 9 13 5 

각 조합이 각 시도의 결과를 만족하는지?

만든 조합 리스트와 입력한 정수를 intersection한 길이가 ans와 같은지
하나라도 다르면 cnt하지 않고 다음 조합 구하기
'''

from itertools import combinations

def solution(n, q, ans):
    comb_list = list(combinations(range(1,n+1), 5))
    #print(comb_list)    
    
    result = 0
    for c in comb_list:
        for i, t in enumerate(q):
            a = ans[i]
            if a != len(set(c) & set(t)):
                break
        else:
            result += 1
    print(result)
    return result
            