from collections import defaultdict
def solution(players, callings):
    '''
    링크드 리스트로 만들기
    
    딕셔너리로 인덱스를 담기
    딕셔너리를 통해 순위에 바로 접근하기
    인덱스가 0이 아니면 앞사람과 인덱스 바꾸기
    
    '''
    rank = defaultdict(int)
    for i in range(len(players)):
        rank[players[i]] = i
    #print(rank)
    for me in callings:
        me_r = rank[me]
        other = players[me_r-1]
        rank[me] -= 1 # 순위 조정
        rank[other] += 1
        players[me_r] = other # 순위 반영
        players[me_r-1] = me
    #print(players)
    return players
                        