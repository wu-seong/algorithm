def solution(s):
    # 길이 확인하기
    length = len(s)
    if length != 4 and length != 6:
        return False
    # 숫자인지 확인하기
    for c in s:
        if not c.isnumeric():
            return False
    return True