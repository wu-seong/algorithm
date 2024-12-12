'''
모든 종류의 보석을 담고있는 가장 짧은 구간 구하기, 여러개일 시에는 더 앞에 있는 것

처음부터 스캔하면서 다음 것이 맨 앞 것과 같으면 맨 앞 자르기 (현재 보석의 개수는 딕셔너리로 유지)
자른 뒤에
마지막 것 잘라도 카운트가 0이 아니면 계속 자르기 

아니면 그냥 추가 
현재 key의 개수가 전체 보석의 개수가 되면 현재 구간 길이 최솟값 비교 및 저장

계속 이어가서

'''
from collections import defaultdict

def solution(gems):
    n = len(set(gems))
    current_gems = defaultdict(int)
    start = 0
    end = 0
    min_range = len(gems)
    result = [1,len(gems)]
    for i, g in enumerate(gems):
        end = i
        current_gems[g] += 1
        if gems[start] == g: # 시작잼이 현재와 같으면 앞에 자르기
            while start < end :
                s_gem = gems[start]
                if not current_gems[s_gem] - 1: # 제거할 때 0이면 제거하지 않음
                    break
                current_gems[s_gem] -= 1
                start += 1
                
        if len(current_gems.keys()) == n: # 모든 보석을 담는 범위
            if end - start + 1 < min_range: # 범위 길이 최솟값 비교
                min_range = end - start + 1
                result = [start+1, end+1]
    print(result)
    return result
            
            
                
        
        
    