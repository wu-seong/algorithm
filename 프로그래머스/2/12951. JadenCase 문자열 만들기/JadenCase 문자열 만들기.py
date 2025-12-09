def to_upper(ch):
    return chr(ord(ch) - 32)
def to_lower(ch):
    return chr(ord(ch) + 32)
def is_upper(ch):
    return ord('A')<= ord(ch) <=ord('Z')
def is_lower(ch):
    return ord('a')<= ord(ch) <=ord('z')
def solution(s):
    # 이전 저장했던 문자가 공백이고 첫 글자가 소문자이면 -> 대문자
    # 이전 저장했던 글자가 공백이 아니고 첫 글자가 대문자이면 -> 소문자
    # 마지막 글자가 단어의 시작일 수도 있음
    # 돌고 나서 마지막 한번 더 체크
    result = to_upper(s[0]) if is_lower(s[0]) else s[0]
    last = s[0]
    for ch in s[1:]:
        if last == ' ' and is_lower(ch):
            result += to_upper(ch)
        elif last != ' ' and is_upper(ch):
            result += to_lower(ch)
        else:
            result += ch
        last = ch
    print(result)
    return result
            
    