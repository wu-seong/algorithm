def solution(s):
    # 문자열을 배열로 바꾸기
    array_s = list(s)
    # 배열을 정렬하기
    array_s.sort(reverse=True)
    # 다시 문자열로 바꾸기
    return "".join(array_s)