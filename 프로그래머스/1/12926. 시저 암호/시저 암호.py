def solution(s, n):
    # 문자열 순회하며 문자 -> 아스키 코드 -> 밀기 -> 문자로 변환하여 새 문자열에 넣기
    # 대소문자 구분해서 밀기
    # 공백은 체크하며 그냥 복사하기
    new_s = []
    for c in s:
        if c == ' ':
            new_s.append(' ')
            continue
        ascii = ord(c)
        if ascii >= ord('a'):
            ascii = ( (ascii - ord('a') + n) % (ord('z') - ord('a') + 1) ) + ord('a')
        else:
            ascii = ( (ascii - ord('A') + n) % (ord('Z') - ord('A') + 1) ) + ord('A')
        new_s.append(chr(ascii))
    #print("".join(new_s))
    return "".join(new_s)