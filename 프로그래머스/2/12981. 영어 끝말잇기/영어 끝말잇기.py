def end(index,n):
    #print(index, n)
    return [(index%n)+1, (index//n)+1]
def solution(n, words):
    # 현재 단어의 첫 글자가 이전 단어의 마지막 글자와 같은지 확인
    # 이전에 나왔던 단어인지 확인 -> set에 나온 단어 저장
    # 인덱스를 n으로 나누고 + 1을 한 것이 번호
    # 차례는 인덱스를 n으로 나눈 몫 + 1
    previous_c = words[0][-1]
    previous_words = set([])
    previous_words.add(words[0])
    for i in range(1,len(words)):
        if words[i][0] != previous_c or words[i] in previous_words:
            return end(i,n)
        previous_c = words[i][-1]
        previous_words.add(words[i])
    return [0,0]
