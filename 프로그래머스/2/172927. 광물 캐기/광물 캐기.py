from collections import defaultdict
def solution(picks, minerals):
    '''
    현재 곡괭이가 최대 효율을 내면서 사용을 해야함
    5개씩 캐니까 50개의 문자열이면 총 3의 10승 = 약 6만
    완탐으로 하면 될듯?
    
    dfs를 통해서 곡괭이 하나 선택하고 picks에서 줄이기
    minerals에서 현재 곡괭이로 얻는 피로도 구하기
    카운트가 0인 곡괭이는 사용할 수 없음
    모든 곡괭이가 0이 되거나 깊이가 10이면 끝
    
    '''
    fatigue_table = defaultdict(dict)
    fatigue_table['diamond']['diamond'] = 1
    fatigue_table['diamond']['iron'] = 1
    fatigue_table['diamond']['stone'] = 1
    fatigue_table['iron']['diamond'] = 5
    fatigue_table['iron']['iron'] = 1
    fatigue_table['iron']['stone'] = 1
    fatigue_table['stone']['diamond'] = 25
    fatigue_table['stone']['iron'] = 5
    fatigue_table['stone']['stone'] = 1
    #print(fatigue_table)
    mines = ["diamond", "iron", "stone"]
    result = float('inf')
    n = len(minerals)
    def dfs(level, fatigue, pickax):
        nonlocal picks, result
        #print(level, fatigue, pickax, picks)
        if level == n//5: # 현재 곡괭이로 캐는 광물이 마지막일 때 
            for i in range(level*5, level*5 + n % 5):
                target = minerals[i]
                fatigue += fatigue_table[pickax][target]
            #print("결과", fatigue)
            result = min(result, fatigue)
            return 
        
        for i in range(level*5,(level+1)*5): # 현재 곡괭이로 캐기
            target = minerals[i]
            fatigue += fatigue_table[pickax][target]
        
        for i, pick in enumerate(picks): # 다음 곡괭이가 있으면 다음 곡괭이 들기
            if picks[i] > 0:
                picks[i] -= 1
                dfs(level+1, fatigue, mines[i])
                picks[i] += 1
        if sum(picks) == 0: # 다음 들 곡괭이가 없으면 현재 값 비교
            #print("결과", fatigue)
            result = min(result, fatigue)
            
    for i, mine in enumerate(mines):
        picks[i] -= 1
        if picks[i] >= 0:
            dfs(0, 0, mine)
        picks[i] += 1
    #print(result)
    return result
        
    