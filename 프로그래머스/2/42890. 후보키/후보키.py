from itertools import combinations
def solution(relation):
    '''
    모든 조합을 구하기
    
    각 조합이 유일성과 최소성을 만족하는 지를 확인하기
    
    각 모든 레코드의 각 컬럼의 값을 가져와서 튜플로 만들기(컬럼 순서대로)
    겹치는 튜플이 없다면 유일성을 만족하는 것임
    
    1개만 뽑는 조합은 유일성만 만족하면 후보키임
    따라서 위의 과정 다음 후보키 리스트에 넣기
    
    n개 뽑는 조합은 유일성을 검사하기 전에 최소성을 먼저 검사한다.
    지금까지 구한 후보키 중 현재 조합에 포함되는 것이 있으면 pass
    
    따라서 1~n까지 순서대로 후보키를 구하면 된다.
    '''
    n = len(relation[0])
    
    cnt = 0
    c_key_list = set()
    for i in range(1,n+1):
        combs = combinations(range(n), i)

        for column in combs: # 각각의 조합 확인 (0,1), (0,2) ...
            if i != 1: 
                #print(i, column, c_key_list)
                contain = False 
                for c_key in c_key_list: # 후보키 중 포함하고 있는것이 있는지 확인
                    for key_column in c_key: # 각각의 요소가 모두 튜플안에 있는지
                        if not key_column in column: # 포함되지 않는 것이 있으면 o
                            break
                    else: # 모든 요소가 현재 조합에 포함되면 최소성 만족x 
                        #print(c_key, column)
                        contain = True
                        break                            
                if contain:
                    continue
            unique = set()
            for record in relation: # 유일성 확인 (100, ryan, music, 2), () ...
                temp = []
                for index in column: # 만들고
                    temp.append(record[index])
                
                if tuple(temp) in unique:
                    break
                else:
                    unique.add(tuple(temp))
            else:
                c_key_list.add(column)
    print("후보키", c_key_list)
    return len(c_key_list)
                    
                
                
            
        