from collections import defaultdict
def solution(weights):
    '''
    몸무게 100~ 1000 중 두 개를 골라서
    100 200
    본인과 같은 짝궁 추가
    2를 곱한 것이 1000이하이면 추가
    본인은 2 상대는 3곱한 것이 1000이하이면 추가
    본인은 3 상대는 4곱한 것이 1000이하이면 추가
    1:1, 1:2 2:3, 3:4 이 중 만족하는 쌍이 있으면 추가 [ (100,200) ]
    '''
    pair_list = []
    for i in range(1,1001):
        if i >= 100 and i*2 <= 1000:
            pair_list.append((i,i*2))
        if i*2 >= 100 and i*3 <= 1000:
            pair_list.append((i*2,i*3))
        if i*3 >= 100 and i*4 <= 1000:
            pair_list.append((i*3,i*4))
    '''
    => 1,000,000
    
    weights를 돌면서 100~1000까지의 무게가 얼마나 나왔는지를 카운팅
    
    미리 구한 비율을 만족하는 쌍을 순회하면서 100만
    n에 있는 사람 수 * n+a에 있는 사람 수
    n == n+a 같은 수이면 cnt(cnt+1)/2
    
    100,100, 101,101 ... 1000,1000 ... 180, 360 ... 180, 270 ... 
    '''
    w_count = defaultdict(int)
    for w in weights:
        w_count[w] += 1
    cnt = 0
    for i in range(100,1001):
         if w_count[i] > 1: # 1보다 크면 n명 중 2명 조합 구하기
            cnt += (w_count[i] * (w_count[i] - 1)) / 2
    for pair in pair_list:
        a,b = pair
        cnt += w_count[a] * w_count[b] # 나머지는 각 몸무게를 가진 사람을 각자 뽑은 곱
            
    #print(cnt)
    return cnt
            
        
    