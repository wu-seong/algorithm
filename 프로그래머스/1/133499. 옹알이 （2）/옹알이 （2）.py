def solution(babbling):
    # 각 단어 당 발음할 수 있는지를 체크하기 100 * 15 * 4 정도 - 충분
    
    # 만약 발음할 수 있는 거면 continue
    # 발음 할 수 있는 리스트에 없으면 false
    # 이전과 같은 발음이어도 false
    # 끝까지 통과하면 +1
    cnt = 0
    can_two = ["ye","ma"]
    can_three = ["aya","woo"]
    for word in babbling:
        can = True
        i = 0
        previous_word = ""
        while(i<len(word)):
            #print(previous_word, word[i:i+2] ,word[i:i+3])
            # 두 글자 체크
            if i+2 <= len(word) and word[i:i+2] in can_two and word[i:i+2] != previous_word:
                previous_word = word[i:i+2]
                i += 2
                continue
            # 세 글자 체크
            if i+3 <= len(word) and word[i:i+3] in can_three and word[i:i+3] != previous_word:
                previous_word = word[i:i+3]
                i += 3
                continue
            can = False
            break
            
        if can:
            cnt += 1
    print(cnt)
    return cnt
            