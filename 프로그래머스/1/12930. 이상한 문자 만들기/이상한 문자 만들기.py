def solution(s):
    strange_list = []
    # 순회하면서 복사하는데 짝수면 대문자, 홀수면 소문자로
    # 만약 공백이 나오면 pass하고 문자가 나오면 다시 짝수부터 세기
    # 각 단어별로 나누기
    pair = True
    for c in s:
        if c == ' ': 
            pair = True
            strange_list.append(' ')
            continue
        if pair:
            strange_list.append(c.upper())
        else:
            strange_list.append(c.lower())
        pair = not pair
    return("".join(strange_list))