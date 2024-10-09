def solution(cards1, cards2, goal):
    # 완전탐색 
    # 중간에 삽입
    
    # 각 뭉치의 다음 순서에 나올 것을 저장, 비교해서 둘 다 아니면 no
    # 둘 중 하나면 다음 순서에 나올 것 갱신
    # goal을 순회하면서 cards1, cards2에 나올 다음 단어를 저장하기 
    next1, next2 = 0,0
    len1 = len(cards1)
    len2 = len(cards2)
    for word in goal:
        if next1 < len1 and word == cards1[next1]:
            next1 += 1
        elif next2 < len2 and word == cards2[next2]:
            next2 += 1
        else:
            return "No"
    return "Yes"