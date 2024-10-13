from collections import defaultdict 
def solution(clothes):
    # 최소 1개는 선택해야한다.
    # 종류당 1개씩만 선택할 수 있다.
    # 의상 1개 - 모든 의상의 수
    # 의상 2개 
    # 서로 다른 n(2<=n<=4)개를 뽑는데 같은 종류이면 카운팅하지 않는다
    # 각 의상마다 어떤 종류인지를 바로 알 수 있도록 딕셔너리에 저장
    # 30c1 + 30c2 + 30c3 + 30c4 충분(인줄 알았는데 아님, 종류가 30개일 수도 있다.) 
    # -> 다른 방법 필요
    
    # 각 종류 마다 key, value를 set으로 저장하기
    # key에서 종류를 1~n개를 뽑아 각 종류의 수만큼 곱한다.
    # 근데 이미 key를 뽑는 것에서 30c15인데 ?
    
    # 그냥 각 종류 마다 일단 개수를 센다.
    # 각 종류마다 1개를 선택하거나 선택하지 않는 경우를 곱연산 한다.
    c_dict = defaultdict(int)
    for cloth, c_type in clothes:
        c_dict[c_type] += 1
    result = 1
    for key in c_dict:
        result *= c_dict[key] + 1
    print(result)
    return result-1
    
    
# 선택하지 않는 것을 선택한다고 생각하면 곱연산이 가능하다.
# 1~n까지의 모든 조합을 구하는 것은 각 요소에 대해 선택/선택하지 않는 모든 경우를 구하고 모두 선택하지 않는 경우를 빼는 것과 같다.
# combinations는 크기보다 큰 조합을 뽑는 경우 빈 리스트를 반환한다.