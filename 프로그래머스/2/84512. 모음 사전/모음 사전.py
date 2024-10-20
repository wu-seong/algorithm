def make_word(n, s, level):
    global words
    if level == n:
        words.append(s)
        return
    l = "AEIOU"
    for a in l:
        make_word(n,s+a,level+1)
    
words = []
def solution(word):
    global words
    # 만들 수 있는 모든 단어를 만들기 5 + 25 + 125 + 625 + 3125 = 3905
    # 1개짜리 모두 만들기
    # 모음 하나씩 고르기

    # 2개짜리 모두 만들기
    # 모음 고르고 또 하나 고르기
    # 사전순으로 정렬하기
    # word찾아 인덱스 출력
    a = "AEIOU"
    for i in range(1,6):
        make_word(i,"",0)
    words.sort()
    #print(words.index(word)+1)
    return words.index(word)+1