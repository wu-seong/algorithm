def solution(s):
    # 모든 알파벳을 소문자로 바꾸기
    s = s.lower()
    # 각 단어 공백 기준으로 구분하기
    new_s = []
    for word in list(s.split(" ")):
        if word == "": # 연속해서 나오면 그대로
            new_s.extend(" ")
            continue
        word_list = list(word)
        if word[0].isalpha():
            word_list[0] = word[0].upper()
        word_list.append(" ")
        new_s.extend(word_list)
    new_s = new_s[:-1]
    #print("".join(new_s))
    return "".join(new_s)
    # 각 단어의 첫 글자가 알파벳이면 대문자로 바꾸기 